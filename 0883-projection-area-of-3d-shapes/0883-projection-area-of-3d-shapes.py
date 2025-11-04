class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(i > 0 for s in grid for i in s)
        xz = sum(max(s) for s in grid)
        yz = sum(max(s[i] for s in grid) for i in range(len(grid)))
        return xy + xz + yz