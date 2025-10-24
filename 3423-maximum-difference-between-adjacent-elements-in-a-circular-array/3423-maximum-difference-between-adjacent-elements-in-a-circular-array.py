class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        mx = abs(nums[0] - nums[-1])

        for num1, num2 in pairwise(nums):
            mx = max(mx, abs(num1 - num2))

        return mx    