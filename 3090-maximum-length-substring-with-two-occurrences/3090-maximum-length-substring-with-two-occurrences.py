class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        f = {}
        mx = 0

        for r in range(len(s)):
            f[s[r]] = f.get(s[r], 0) + 1

            while f[s[r]] > 2:
                f[s[l]] -= 1
                l += 1

            mx = max(mx, r - l + 1)

        return mx