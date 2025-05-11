class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1 or n == 2: return n

        return 2 ** n.bit_length()
        