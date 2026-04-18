# Added using AI
class Solution:
    def revnum(self, a: int) -> int:
        if a // 10 == 0:
            return a
        return int(str(a)[::-1])

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.revnum(n))