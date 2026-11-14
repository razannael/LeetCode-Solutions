class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        n, mn = len(nums), inf
        acc = list(accumulate(nums, initial = 0))
        
        for left in range(n):
            for rght in range(left+1, n+1):
                
                sm, length = acc[rght] - acc[left], rght - left
                if l <= length <= r and 0 < sm < mn: mn = sm 
        
        return -1 if mn == inf else mn