class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        maxi = (n * (n-1)//2)
        if k > maxi:
            return 0
        if k == 0 or k == maxi:
            return 1

        mod = 10 ** 9 + 7

        dp = [[0]*(k+1) for _ in range(n+1)]

        for i in range(1, n+1):
            dp[i][0] = 1

        dp[2][1] = 1

        for i in range(3,n+1):
            maxi = min(k, i*(i-1)//2)
            for j in range(1,  maxi + 1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] 
                if j>=i:
                    dp[i][j] -= dp[i-1][j - i]
                dp[i][j] = (dp[i][j] + mod) % mod

        return dp[n][k]