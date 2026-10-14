class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        if s > n * 9: return ''
        q, r = divmod(s, 9)
        res = '9' * q + (str(r) if r else '')
        return res + '0' * (n - len(res))
        