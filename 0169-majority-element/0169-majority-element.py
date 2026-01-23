class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = None
        score = 0
        for n in nums:
            if score == 0:
                curr = n
            score += 1 if curr == n else - 1
        return curr