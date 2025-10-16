class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = sum(1 for c in s if c in "ueoai")
        if cnt == 0: return False
        return True