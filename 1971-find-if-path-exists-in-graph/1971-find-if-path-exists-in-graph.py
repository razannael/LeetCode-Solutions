class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:

        d = defaultdict(list)
        stack = deque([start])
        visited = {start}

        for i, j in edges: 
            d[i].append(j)
            d[j].append(i)
            
        while stack:
            node = stack.popleft()
            if node == end: return True

            for x in d[node]:
                if x not in visited:
                    visited.add(x)
                    stack.append(x)
                    
        return False