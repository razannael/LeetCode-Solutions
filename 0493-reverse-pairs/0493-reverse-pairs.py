class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        slist = SortedList()
        res = 0
        for i, x in enumerate(nums):
            res += i - slist.bisect_right(2 * x)
            slist.add(x)
        return res