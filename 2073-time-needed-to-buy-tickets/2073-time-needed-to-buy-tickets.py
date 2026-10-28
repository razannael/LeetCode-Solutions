class Solution:
    def timeRequiredToBuy(self, ti: List[int], k: int) -> int:

        s = 0
        n = len(ti)

        for i in range(n):

            if i <= k:
                s += min(ti[i], ti[k])

            else:
                s += min(ti[i], ti[k] - 1)

        return s