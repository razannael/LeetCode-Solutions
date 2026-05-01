class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        F = sum(i * nums[i] for i in range(n))
        total_sum = sum(nums)

        maxF = F

        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            maxF = max(maxF, F)

        return maxF