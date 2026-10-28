class Solution:
    def largestAltitude(self, a: List[int]) -> int:
        return max(accumulate(a,initial=0))