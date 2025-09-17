class Solution:
    def countStableSubsequences(self, nums: list[int]) -> int:
        e1, e2, o1, o2 = 0, 0, 0, 0
        for x in nums:
            if x & 1:
                se1, se2, so1 = e1, e2, o1
                o2 = (o2 + so1) % (10**9 + 7)
                o1 = (o1 + se1 + se2 + 1) % (10**9 + 7)
            else:
                se1, so1, so2 = e1, o1, o2
                e2 = (e2 + se1) % (10**9 + 7)
                e1 = (e1 + so1 + so2 + 1) % (10**9 + 7)
        return (e1 + e2 + o1 + o2) % (10**9 + 7)