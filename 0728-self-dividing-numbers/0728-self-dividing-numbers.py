from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            n = i

            while n > 0:
                r = n % 10
                if r == 0:
                    break
                if i % r != 0:
                    break
                else:
                    n //= 10

            if n == 0:
                res.append(i)

        return res