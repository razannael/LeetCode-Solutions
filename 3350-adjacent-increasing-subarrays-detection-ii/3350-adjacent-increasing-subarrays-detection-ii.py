class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n, Len, prev, k=len(nums), 1, 0, 0
        for i in range(1, n):
            if nums[i]>nums[i-1]: Len+=1
            else:
                k=max(k, Len//2, min(Len, prev))
                prev=Len
                Len=1
        return max(k, Len//2, min(Len, prev))
        