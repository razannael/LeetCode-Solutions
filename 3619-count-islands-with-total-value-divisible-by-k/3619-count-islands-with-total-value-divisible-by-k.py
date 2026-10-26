class Solution:
    def helpIslands(self, grid, i, j, m, n, sum_ref):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return

        sum_ref[0] += grid[i][j]
        grid[i][j] = 0

        self.helpIslands(grid, i - 1, j, m, n, sum_ref)
        self.helpIslands(grid, i + 1, j, m, n, sum_ref)
        self.helpIslands(grid, i, j - 1, m, n, sum_ref)
        self.helpIslands(grid, i, j + 1, m, n, sum_ref)

    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    sum_ref = [0]
                    self.helpIslands(grid, i, j, m, n, sum_ref)
                    if sum_ref[0] % k == 0:
                        count += 1
        return count