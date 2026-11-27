class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans=[]

        def sol(nums,num,target):
            
            if target==0:
                ans.append(nums[:])
                return
            if target<0:
                return
            if num>=len(candidates):
                return

            
            nums.append(candidates[num])
            sol(nums,num,target-candidates[num])
            nums.pop()
            
            sol(nums,num+1,target)
        
        sol([],0,target)
        return ans



            



        