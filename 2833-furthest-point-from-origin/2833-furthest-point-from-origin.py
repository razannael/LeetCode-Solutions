class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        return len(m) - min(m.count('L'), m.count('R'))*2