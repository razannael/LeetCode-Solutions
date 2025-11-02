class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        nums.sort(reverse = True, key=abs)

        res = 1

        res*=abs(nums[0])
        res*=abs(nums[1])
        res*=abs(100000)

        return res