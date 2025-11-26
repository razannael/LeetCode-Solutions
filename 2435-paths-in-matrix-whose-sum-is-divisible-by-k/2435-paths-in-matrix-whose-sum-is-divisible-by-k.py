class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        @cache
        def dp(r: int, c: int, cur_sum: int) -> int:
            if r == m - 1 and c == n - 1: return int(cur_sum == 0)
            res = 0
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n: continue
                res = (res + dp(nr, nc, (cur_sum + grid[nr][nc]) % k)) % mod
            return res

        return dp(0, 0, grid[0][0] % k) % mod