class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)

        while b!=0:
            temp = b
            b = a % b
            a = temp
        return a
        