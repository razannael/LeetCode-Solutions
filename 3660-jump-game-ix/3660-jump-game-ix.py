class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_min = nums[:]
        mini = nums[-1]
        res = []

        for i in range(n-2,-1,-1):
            mini = min(mini, suffix_min[i])
            suffix_min[i] = mini
        
        maxi = 0
        for i in range(n):
            maxi = max(maxi, nums[i])
            if i == n-1 or maxi <= suffix_min[i+1]:
                res.extend([maxi] * ((i+1)-len(res)))

        return res       
        