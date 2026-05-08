class Solution:
    def productExceptSelf(self, nums: List[int]) -> list[int]:
        n = len(nums)
        res = []
        prefix = [1] * (n+1)
        suffix = [1] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res