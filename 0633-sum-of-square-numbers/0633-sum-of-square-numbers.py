# a^2 + b^2 = c
# c = 5
# Find a and b such that a^2 + b^2 = c
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a * a)

            if b == int(b):
                return True
        return False