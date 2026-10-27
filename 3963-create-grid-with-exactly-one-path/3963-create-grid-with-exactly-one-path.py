class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n if i == 0 else "#" * (n - 1) + "." for i in range(m)]