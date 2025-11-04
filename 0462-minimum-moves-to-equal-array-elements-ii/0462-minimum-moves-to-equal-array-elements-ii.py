class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums)//2]
        result = 0
        for i in nums:
            result+=abs(mid-i)
        return result