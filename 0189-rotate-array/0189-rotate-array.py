class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        newK = k % n
        nums2 = [0] * n
        for i in range(n):
            nums2[(i+k)%n] = nums[i]
        for i in range(n):
            nums[i] = nums2[i]