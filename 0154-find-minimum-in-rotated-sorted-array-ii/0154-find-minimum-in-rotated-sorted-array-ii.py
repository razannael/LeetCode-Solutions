class Solution:
    def findMin(self, nums: List[int]) -> int:
        return  nums[0] if nums[0]<nums[-1]  else nums[
            bisect_left(nums, True, key=lambda x: x<nums[0], 
                hi=next((i for i in range(len(nums)-1,-1,-1) if nums[i]<nums[0]), 0)
            )
        ]
        