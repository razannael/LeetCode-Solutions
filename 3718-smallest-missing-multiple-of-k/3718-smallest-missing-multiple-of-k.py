class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        current = k
        while current in s:
            current +=k
        return current