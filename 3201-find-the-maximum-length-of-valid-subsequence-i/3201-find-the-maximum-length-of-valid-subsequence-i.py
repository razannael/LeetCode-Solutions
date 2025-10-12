class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n=len(nums)
        if n==2: return 2
        z=nums[0]&1
        Len=[1-z, z, 1]
        for xx in nums[1:]:
            x=xx&1
            Len[x&1]+=1
            if x!=z:
                Len[2]+=1
                z=1-z
        return max(Len)