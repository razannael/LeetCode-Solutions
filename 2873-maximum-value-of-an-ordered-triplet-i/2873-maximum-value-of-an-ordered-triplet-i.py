class Solution(object):
    def maximumTripletValue(self, nums):
        maxTriplet = 0
        for i in range(len(nums)):
            for k in range(len(nums) - 1, i, -1):
                j = i + 1
                while j < k:
                    maxTriplet = max(maxTriplet, (nums[i] - nums[j]) * nums[k])
                    j += 1
        return max(0, maxTriplet)