class Solution:
    def countNoZeroPairs(self, n: int) -> int:

        lenN = len(str(n))
        digits = list(map(int, str(n)))[::-1]

        @lru_cache(None)
        def solve(pos, carry, lenA, lenB):
            if pos == lenN:
                return int(carry == 0)

            rangeA = range(1, 10) if pos < lenA else (0,)
            rangeB = range(1, 10) if pos < lenB else (0,)

            numWays = 0
            for da in rangeA:
                for db in rangeB:
                    summ = da + db + carry
                    if summ % 10 == digits[pos]:
                        numWays += solve(pos + 1, summ // 10, lenA, lenB)
            return numWays

        totalPairs = 0
        for lenA in range(1, lenN + 1):
            for lenB in range(1, lenN + 1):
                totalPairs += solve(0, 0, lenA, lenB)

        return totalPairs