class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        for i, num in enumerate(nums):
            res += round(math.cos(math.pi * i) * num)
        return res