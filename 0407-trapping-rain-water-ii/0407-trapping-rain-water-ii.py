from heapq import heappush, heappop
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Add all boundary cells to the heap
        for i in range(m):
            for j in [0, n - 1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        for j in range(n):
            for i in [0, m - 1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        trapped_water = 0
        while heap:
            height, x, y = heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    trapped_water += max(0, height - heightMap[nx][ny])
                    heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        
        return trapped_water