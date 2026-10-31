class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        right = [[0] * n for _ in range(m)]  # entered this cell moving right
        down  = [[0] * n for _ in range(m)]  # entered this cell moving down

        right[0][0] = 1  # start: count it once

        for i in range(m):
            for j in range(n):
                # coming from the left cell
                if j > 0:
                    if grid[i][j-1] == 0:
                        right[i][j] += right[i][j-1] + down[i][j-1]
                    else:  # mirror: only paths that entered it moving down get pushed right
                        right[i][j] += down[i][j-1]

                # coming from the cell above
                if i > 0:
                    if grid[i-1][j] == 0:
                        down[i][j] += right[i-1][j] + down[i-1][j]
                    else:  # mirror: only paths that entered it moving right get pushed down
                        down[i][j] += right[i-1][j]

                right[i][j] %= MOD
                down[i][j] %= MOD

        return (right[m-1][n-1] + down[m-1][n-1]) % MOD
