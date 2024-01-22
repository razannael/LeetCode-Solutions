class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
     uniques = set()
     duplicate = 0
     for n in nums:
         if n in uniques:
             duplicate = n
         uniques.add(n)   
     for i in range(1 , len(nums)+1):
         if i not in uniques:
             return [duplicate , i]
