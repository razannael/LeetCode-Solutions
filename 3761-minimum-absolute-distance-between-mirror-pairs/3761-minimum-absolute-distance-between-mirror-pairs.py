class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        res = 100000
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                res = min(res, i - seen[n])
            seen[int(str(n)[::-1])] = i

        return -(res == 100000) | res