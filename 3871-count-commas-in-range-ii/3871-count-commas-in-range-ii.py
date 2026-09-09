class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        threshold = 1000

        while threshold <= n:
            ans += n - threshold + 1
            threshold *= 1000

        return ans