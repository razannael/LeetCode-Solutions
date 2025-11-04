class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:

        isReduced = lambda x: gcd(*x) == 1

        pairs = filter(isReduced, combinations(range(1,n+1),2))

        return [f"{x}/{d}" for x, d in pairs]
        