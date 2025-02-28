class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        before, after = 0, len(matrix)*len(matrix[0])
        while before < after - 1:
            center = (before + after) // 2
            r,c = self.fromIndToCell(center, len(matrix[0]))
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                before = center + 1
            else:
                after = center

        if before == len(matrix)*len(matrix[0]):
            return False

        r,c = self.fromIndToCell(before, len(matrix[0]))
        return matrix[r][c] == target
            

    def fromIndToCell(self, i, ncols):
        r = i // ncols
        c = i % ncols
        return r, c