class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        count = 0
        i = 1000

        while i != n:
            count += 1
            i += 1

        return count + 1