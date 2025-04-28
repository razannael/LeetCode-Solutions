class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.countPairsWithSumLessThan(nums, upper + 1) - self.countPairsWithSumLessThan(nums, lower)

    def countPairsWithSumLessThan(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count