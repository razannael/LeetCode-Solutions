class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0]
        
        for indx in range(0, len(A) - 1):
            # assuming that A[indx] is the max val
            min_val = min(A[0] + K, A[indx + 1] - K)
            max_val = max(A[indx] + K, A[-1] - K)
            res = min(res, max_val - min_val)

        return res