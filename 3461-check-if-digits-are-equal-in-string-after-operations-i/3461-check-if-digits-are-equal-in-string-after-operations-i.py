class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(c) for c in s]
        n = len(digits)
        while n > 2:
            for i in range(n - 1):
                digits[i] = (digits[i] + digits[i + 1]) % 10
            n -= 1
        return digits[0] == digits[1]