class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m ,n = len(grid), len(grid[0])
        r ,c = 0, n-1
        count = 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                count += (m - r)
                c -= 1
            else:
                r += 1
        return count
