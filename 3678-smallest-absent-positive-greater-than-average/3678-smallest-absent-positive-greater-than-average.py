class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        return min(i for i in range(1, 202) if i not in nums and i > sum(nums)/len(nums))
