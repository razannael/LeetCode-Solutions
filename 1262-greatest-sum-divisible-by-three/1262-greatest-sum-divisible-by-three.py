class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
                    
        n = sum(nums)                                               # <-- 1)
        nDiv3 = n%3
        if nDiv3 == 0: return n
        
        terms = [0]+ sorted(filter(lambda x:x%3 != 0, nums))[:4]    # <-- 2)

        return n - min(map(sum,filter                               # <-- 3)
            (lambda x: (x[0]+x[1])%3 == nDiv3, combinations(terms,2))))