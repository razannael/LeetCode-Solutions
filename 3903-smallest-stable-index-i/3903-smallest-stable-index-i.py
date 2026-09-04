class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_ele = float('-inf')
        min_ele_prefix = [0]*len(nums)
        min_ele_prefix[-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            min_ele_prefix[i] = min(nums[i],min_ele_prefix[i+1])
        for i in range(len(nums)):
            max_ele = max(nums[i], max_ele)
            if max_ele-min_ele_prefix[i]<=k:
                return i
        return -1