from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        H = len(heights)
        W = len(heights[0])

        queue = deque([])
        queue.append((0, 0))

        cost = { (row, col): float('inf') for col in range(W) for row in range(H) }
        cost[(0, 0)] = 0

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def inside(row, col):
            return 0 <= row < H and 0 <= col < W
        
        while queue:
            row, col = queue.popleft()
            current_height = heights[row][col]
            current_cost = cost[(row, col)]

            for d_row, d_col in directions:
                new_row = row + d_row
                new_col = col + d_col

                if inside(new_row, new_col):
                    neighbor_height = heights[new_row][new_col]
                    new_cost = max(current_cost, abs(neighbor_height - current_height))
                    if new_cost < cost[(new_row, new_col)]:
                        cost[(new_row, new_col)] = new_cost
                        queue.append((new_row, new_col))
        
        return cost[(H - 1, W - 1)]