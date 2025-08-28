from typing import List

class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        # Sort by absolute value
        nums.sort(key=abs)
        n = len(nums)
        ans = 0
        j = 1

        # Two pointers: for each i, expand j while |nums[j]| <= 2 * |nums[i]|
        for i in range(n):
            if j < i + 1:
                j = i + 1
            while j < n and abs(nums[j]) <= 2 * abs(nums[i]):
                j += 1
            ans += (j - i - 1)

        return ans
