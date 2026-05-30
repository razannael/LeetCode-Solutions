import bisect

class MaxSegmentTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, index: int, value: int, node: int, start: int, end: int):
        if index < start or index > end:
            return
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, value, 2 * node, start, mid)
        else:
            self.update(index, value, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l: int, r: int, node: int, start: int, end: int) -> int:
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(l, r, 2 * node, start, mid)
        p2 = self.query(l, r, 2 * node + 1, mid + 1, end)
        return max(p1, p2)


class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        # 1. Dynamically bound the maximum dimension
        max_x = max(q[1] for q in queries)
        
        seg_tree = MaxSegmentTree(max_x + 1)
        # Use a safe infinity bound for the right edge to avoid tree array overflows
        obstacles = [0, float('inf')]
        
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                
                idx = bisect.bisect_left(obstacles, x)
                if obstacles[idx] == x:
                    continue
                    
                left = obstacles[idx - 1]
                right = obstacles[idx]
                
                bisect.insort(obstacles, x)
                
                # Update the new left-hand gap split
                seg_tree.update(x, x - left, 1, 0, max_x)
                
                # Only update the right-hand gap if it falls within our tracked coordinate image space
                if right <= max_x:
                    seg_tree.update(right, right - x, 1, 0, max_x)
                
            elif q[0] == 2:
                target_x = q[1]
                required_sz = q[2]
                
                idx = bisect.bisect_right(obstacles, target_x) - 1
                last_obstacle = obstacles[idx]
                
                # Query the maximum gap up to the last obstacle safely within bounds
                max_available_gap = seg_tree.query(0, last_obstacle, 1, 0, max_x)
                
                # Capture the trailing residual space up to target_x
                residual_gap = target_x - last_obstacle
                
                final_boundary_max = max(max_available_gap, residual_gap)
                
                results.append(bool(final_boundary_max >= required_sz))
                
        return results