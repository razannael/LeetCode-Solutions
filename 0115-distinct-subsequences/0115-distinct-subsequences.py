class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S = len(s)
        T = len(t)
        dp = [[0]*(T+1) for _ in range(S+1)]
        for i in range(S+1):
            dp[i][T] = 1
        for i in range(S-1,-1,-1):
            for j in range(T-1,-1,-1):
                if s[i]==t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]