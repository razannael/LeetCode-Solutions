class Solution(object):
    def countSubarrays(self, nums, k):
        maxi = max(nums)
        left = 0
        maxiOccurence = 0
        res = 0
        for right in range(len(nums)):
            maxiOccurence += nums[right] == maxi
            while maxiOccurence >= k:
                maxiOccurence -= nums[left] == maxi
                left += 1
            res += left
        return res