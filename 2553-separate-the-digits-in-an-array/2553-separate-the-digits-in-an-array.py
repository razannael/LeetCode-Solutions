class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            s = str(num)
            for char in s:
                res.append(int(char))
        return res