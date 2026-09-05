class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # Count frequency of each number
        count = [0] * 102
        for num in nums:
            count[num] += 1
            
        # Cumulative sum to find how many numbers are smaller
        for i in range(1, 102):
            count[i] += count[i - 1]
            
        # Build the result array
        return [0 if num == 0 else count[num - 1] for num in nums]
