class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return [x for x in range(min(nums), max(nums)+1) if x not in (s:=set(nums))]