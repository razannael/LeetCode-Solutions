class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n=len(nums)
        ans=[]
        j=0
        for i, x in enumerate(nums):
            if x==key:
                up=min(n-1, i+k)
                j=max(j, i-k)
                while j<=up:
                    ans.append(j)
                    j+=1
        return ans
        
        