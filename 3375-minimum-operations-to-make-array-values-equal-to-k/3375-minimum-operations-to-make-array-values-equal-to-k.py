class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hasX=0
        xMin=101
        for x in nums:
            hasX|=1<<x
            xMin=min(x, xMin)
        
        if xMin<k: return -1
        B=hasX.bit_count()
        return B-1 if xMin==k else B
        