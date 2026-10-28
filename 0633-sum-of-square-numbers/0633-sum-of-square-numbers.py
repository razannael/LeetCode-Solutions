import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(math.sqrt(c))

        while low <= high:
            k = low ** 2 + high ** 2

            if k == c:
                return True
            elif k < c:
                low += 1
            else:
                high -= 1

        return False