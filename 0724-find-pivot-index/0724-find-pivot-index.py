class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        for i, v in enumerate(nums):
            leftSum += v
            if leftSum == rightSum :
                return i
            rightSum -= v
        return -1