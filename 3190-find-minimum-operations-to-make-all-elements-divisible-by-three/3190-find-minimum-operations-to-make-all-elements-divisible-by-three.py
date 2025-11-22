class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
 
        return sum(map(lambda x: bool(x %3), nums))