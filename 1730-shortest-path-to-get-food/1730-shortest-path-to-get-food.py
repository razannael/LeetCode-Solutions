class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        start = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "*":
                    start.append((i, j, 0))
                    break     
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while start:
            x, y, cnt = start.popleft()
            if grid[x][y] == "X":
                continue
            elif grid[x][y] == "#":
                return cnt
            grid[x][y] = "X"
            for i, j in directions:
                nx, ny = i + x, j + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "X":
                    start.append((nx, ny, cnt + 1))
        return -1



