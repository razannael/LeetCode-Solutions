class Solution:
    def minChanges(self, s: str) -> int:
        it = iter(s)
        return sum(map(ne, it, it))