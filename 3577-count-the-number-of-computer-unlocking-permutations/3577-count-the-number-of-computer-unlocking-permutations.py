class Solution:
    def countPermutations(self, complexity: List[int]) -> int:

        n, initial, fact = len(complexity), complexity[0], 1
        mod_ = 1_000_000_007

        for num in complexity[1:]:
            if num <= initial: return 0

        for i in range(2, n):
            fact*= i
            fact%= mod_

        return fact