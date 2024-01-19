class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        forward = [1]*n
        for i in range(1, n):
            forward[i] *= nums[i-1]*forward[i-1]
        
        # backward = [1]*n
        # for i in range(n-2, -1, -1):
        #     backward[i] *= nums[i+1]*backward[i+1]

        backward = 1
        for i in reversed(range(n)):
            forward[i] *= backward
            backward *= nums[i]
        
        # return [f*b for f,b in list(zip(forward, backward))]
        return forward