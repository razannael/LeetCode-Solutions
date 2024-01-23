class Solution:
    def maxLength(self, arr: List[str]) -> int:
        mySet = set() #to store the concatenated strings
        
         #check if the string overlap with the set
        def overlap (mySet , s):
            c= Counter(mySet) + Counter(s)
            return max(c.values()) >1
   
        def backTrack(n):
            if n == len(arr):
                return len(mySet)
            result = 0
            if not overlap (mySet , arr[n]):  
                for c in arr[n]:
                    mySet.add(c)
                result = backTrack(n+1)
                for c in arr[n]:
                    mySet.remove(c)
            return max(result , backTrack (n +1))
        return backTrack(0)
