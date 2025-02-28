class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        li = [[]]
        nums.sort()
        se = set()
        for val in nums:
            li += [curr + [val] for curr in li]
        for val in li:
            se.add(tuple(val))
        li = []
        for val in se:
            li += [val]
        return li