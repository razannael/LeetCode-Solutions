class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        cm = [n + 1] * (n + 1)   # col_min_y: smallest y in column x
        cM = [0]     * (n + 1)   # col_max_y: largest  y in column x
        rm = [n + 1] * (n + 1)   # row_min_x: smallest x in row    y
        rM = [0]     * (n + 1)   # row_max_x: largest  x in row    y

        # First pass: compute extremes
        for x, y in buildings:
            cm[x] = min(cm[x], y)
            cM[x] = max(cM[x], y)
            rm[y] = min(rm[y], x)
            rM[y] = max(rM[y], x)

        # Second pass: count covered
        covered = 0
        for x, y in buildings:
            if cm[x] < y < cM[x] and rm[y] < x < rM[y]:
                covered += 1

        return covered