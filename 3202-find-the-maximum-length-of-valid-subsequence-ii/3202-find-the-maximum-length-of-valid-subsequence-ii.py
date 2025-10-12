class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0]*k for _ in range(k)]
        for x in nums: 
            x %= k 
            for y in range(k): 
                dp[x][y] = 1 + dp[y][x]
        return max(map(max, dp))