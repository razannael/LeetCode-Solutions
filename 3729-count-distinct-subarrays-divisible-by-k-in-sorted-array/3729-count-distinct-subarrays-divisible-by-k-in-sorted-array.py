class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        prefix = 0
        ans = 0
        freq = {}
        for i in range(len(nums)):
            prefix += nums[i]
            ans += mp.get(prefix%k,0) 
            mp[prefix%k] = mp.get(prefix%k,0)+1
            freq[nums[i]] = freq.get(nums[i],0)+1 
        
        for key,v in freq.items():
            maxi,total,pre = 0,0,0
            innerMp = {0:1}
            for i in range(v):
                pre += key
                total += innerMp.get(pre%k,0) 
                innerMp[pre%k]  = innerMp.get(pre%k,0)+1
                maxi = max(maxi, innerMp[pre%k])
            ans = ans - (total - maxi)-1
        return ans