class Solution:
    def maxArea(self, nums: list[int]) -> int:
        i,j = 0, len(nums) -1
        ans = float("-inf")
        while i<j:
            area = (j-i) * min(nums[i], nums[j])
            ans = max(ans, area)
            if nums[i] <= nums[j]:
                i+=1
            else:
                j-=1
        return ans