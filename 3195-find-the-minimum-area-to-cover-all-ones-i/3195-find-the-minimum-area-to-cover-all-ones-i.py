class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        iMin, iMax, jMin, jMax=1000, -1, 1000, -1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x==0: continue
                iMin=min(iMin, i)
                iMax=max(iMax, i)
                jMin=min(jMin, j)
                jMax=max(jMax, j)
        return (iMax-iMin+1)*(jMax-jMin+1)

             