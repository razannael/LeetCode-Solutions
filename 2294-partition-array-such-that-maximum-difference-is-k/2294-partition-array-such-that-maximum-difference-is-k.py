class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))  # Remove duplicates and sort
        ans = 1
        mn = nums[0]

        for num in nums[1:]:
            if num - mn > k:
                ans += 1
                mn = num

        return ans