class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxOnesLen = 0
        currOnesLen = 0
        zeros = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0 :
               zeros += 1    
            while zeros > 1:
                if nums[j] == 0:
                    zeros-=1
                j+=1
            currOnesLen = i - j + 1
            maxOnesLen = max(currOnesLen , maxOnesLen)
        return maxOnesLen -1 if maxOnesLen > 0 else 0


