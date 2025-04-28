class Solution(object):
    def countSubarrays(self, nums, k):
        count = 0
        sum = 0
        left = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum * (right - left + 1) >= k:
                sum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count