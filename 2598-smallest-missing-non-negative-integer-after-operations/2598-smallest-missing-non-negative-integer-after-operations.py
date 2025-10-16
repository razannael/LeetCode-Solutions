class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        m = Counter([n % value for n in nums])
        for i in range(len(nums)):
            if m[i % value] == 0:
                return i
            m[i % value] -= 1
        return len(nums)