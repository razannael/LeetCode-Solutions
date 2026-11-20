class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 1
        DP = {}
        
        for num in nums:
            a, b = 1, 1
            if num - 1 in DP:
                a = DP[num - 1] + 1
            
            if num in DP:
                b = DP[num] + 1
                
            DP[num] = max(DP.get(num, 0), a)
            DP[num + 1] = max(DP.get(num + 1, 0), b)
            
            ans = max(ans, max(DP[num], DP[num + 1]))
        
        return ans
        