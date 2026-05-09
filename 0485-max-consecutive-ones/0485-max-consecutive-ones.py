class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current=0
        max_count=0
        for num in nums:
            if num == 1:
                current +=1
            else:
                current = 0
            max_count = max(max_count, current)
        return max_count