class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        cnt = [0] * (n + 1)
        ans = []
        
        common = 0
        
        for i in range(n):
            cnt[A[i]] += 1
            if cnt[A[i]] == 2:
                common += 1
            
            cnt[B[i]] += 1
            if cnt[B[i]] == 2:
                common += 1
            
            ans.append(common)
        
        return ans     