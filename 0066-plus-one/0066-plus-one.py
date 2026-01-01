class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        s = str(int("".join(map(str, digits)))+1)
        for i in s:
             res.append(int(i))
        return res