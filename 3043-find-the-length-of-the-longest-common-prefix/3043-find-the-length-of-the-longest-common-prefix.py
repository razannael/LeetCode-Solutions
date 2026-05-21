class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1=set()
        maxi=0
        for num in arr1:
            while num>0:
                set1.add(num)
                num//=10
        for num in arr2:
            while num>0:
                if num in set1:
                    maxi=max(maxi,len(str(num)))
                    break
                num//=10
        return maxi

                    
                    
