class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        
        n = len(nums) - 2
        nums.sort(reverse = True)

        for i in range(n):
         if nums[i] < nums[i + 1] + nums[i + 2]:
            return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0