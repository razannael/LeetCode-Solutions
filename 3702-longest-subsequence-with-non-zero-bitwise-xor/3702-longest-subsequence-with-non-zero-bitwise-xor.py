class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        N = len(nums)
        s = 0
        flag = True
        
        for n in nums:
            s ^= n
            if n != 0:
                flag = False
        
        # All elements are zero
        if flag:
            return 0
        
        # XOR of all elements is zero - remove one element
        if s == 0:
            return N - 1
        
        # XOR of all elements is non-zero - take entire array
        return N