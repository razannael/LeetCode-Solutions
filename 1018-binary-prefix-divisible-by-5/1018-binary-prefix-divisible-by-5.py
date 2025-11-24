class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        num = 0
        
        for n in nums:
            num = (num * 2 + n) % 5
            res.append(num == 0)
            
        return res