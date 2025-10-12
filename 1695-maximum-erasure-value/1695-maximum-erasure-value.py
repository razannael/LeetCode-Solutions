class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter=defaultdict(int) # track count of  elements in the window
        res=i=tot=0
		
        for j in range(len(nums)):
            x=nums[j]   
            tot+=x
            counter[x]+=1
            # adjust the left bound of sliding window until you get all unique elements
            while i < j and counter[x]>1: 
                counter[nums[i]]-=1
                tot-=nums[i]
                i+=1
            
            res=max(res, tot)            
        return res