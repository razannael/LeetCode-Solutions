class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        res = 0
        for m in range(1, 1<<len(a)):
            res += reduce(or_, (v for i,v in enumerate(a) if 1<<i&m)) == reduce(or_,a)

        return res