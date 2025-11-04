class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:

        M, m = max(A), min(A)
        diff, extension = M - m, 2*K
        
        if diff <= extension:
            return 0
        
        else:
            return diff - extension