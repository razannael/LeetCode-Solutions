class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        Z = [0] * n
        L = R = 0
        
        for i in range(1, n):
            if i <= R:
                Z[i] = min(R - i + 1, Z[i - L])
            
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            
            if i + Z[i] - 1 > R:
                L = i
                R = i + Z[i] - 1
        
        return n + sum(Z)