class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        max_length = min((m - 1) // 2, (n - 1) // 2)
        best = []
        heapify(best)
        def rhombusSum(r, c, k):
            result = grid[r][c]
            for s in range(k):
                r += 1
                result += grid[r][c + s + 1]
                result += grid[r][c - s - 1]
            for s in range(k - 1, -1, -1):
                r += 1
                result += grid[r][c + s]
                if s > 0:
                    result += grid[r][c - s]
            return result
        for r in range(m):
            for c in range(n):
                for k in range(max_length + 1):
                    if c >= k and c + k < n and r + 2 * k < m:
                        candidate = rhombusSum(r, c, k)
                        if candidate not in set(best):
                            heappush(best, candidate)
                        if len(best) > 3:
                            heappop(best)
        return sorted(best, reverse = True)