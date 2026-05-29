class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = 0
            for j in str(nums[i]):
                n += int(j)
            nums[i] = n
        return min(nums)