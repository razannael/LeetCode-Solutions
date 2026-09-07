class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1
        last = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            old = dp
            dp = (2 * dp - last[i]) % MOD
            last[i] = old

        return (dp - 1) % MOD