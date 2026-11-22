class Solution:
    def checkString(self, s: str) -> bool:
        s1 = "".join(sorted(s))
        return s1 == s