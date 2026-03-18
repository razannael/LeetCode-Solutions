class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        grid = map(accumulate, grid)                        # <-- 1)
        grid = map(accumulate, zip(*grid))                  # <-- 2)

        return sum(x <= k for row in grid for x in row)     # <-- 3)