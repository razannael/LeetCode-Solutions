class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = set()
        res = []
        for num in nums:
            if(num not in visited):
                visited.add(num)
            else:
                res.append(num)
        return res
        