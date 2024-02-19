class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = set()
        repeating = set()
        for c in s:
            if c in repeating:
                continue
            if c in unique:
                repeating.add(c)
                unique.remove(c)
            else:
                unique.add(c)
        for index in range(len(s)):
            if s[index]  in unique:
                return index
        return -1