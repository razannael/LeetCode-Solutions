from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n,m=len(nums1),len(nums2)

        @lru_cache(None)
        def dp(i,j):
            if i==n or j==m:
                return -inf
            take=nums1[i]*nums2[j]+max(0,dp(i+1,j+1))
            skip1=dp(i+1,j)
            skip2=dp(i,j+1)
            
            return max(take,skip1,skip2)

        return dp(0,0)
        