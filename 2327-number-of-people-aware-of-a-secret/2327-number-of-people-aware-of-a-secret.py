class Solution:
    def peopleAwareOfSecret(self, n: int, d: int, f: int) -> int:
        dp, md = [1] + [0] * (f - 1), 10**9 + 7
        for i in range(1, n):
            dp[i % f] = (md + dp[(i + f - d) % f] - dp[i % f] + (0 if i == 1 else dp[(i - 1) % f])) % md
        return sum(dp) % md