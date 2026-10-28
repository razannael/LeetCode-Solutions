class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]

                if i == 0 and j == 0:
                    dp[j] = {val}
                    continue

                curr = set()

                if i > 0:
                    curr.update(x ^ val for x in dp[j])

                if j > 0:
                    curr.update(x ^ val for x in dp[j - 1])

                dp[j] = curr

        return min(dp[n - 1])    