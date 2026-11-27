class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = nums[0]
        cs = 0        

        for i in nums:
            cs += i
            maxi = max(maxi,cs)
            if cs < 0:
                cs=0

        return maxi