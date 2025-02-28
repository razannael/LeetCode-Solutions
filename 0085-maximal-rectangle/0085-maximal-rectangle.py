class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area

    def maximalAreaOfSubMatrixOfAll1(self, mat, n, m):
        max_area = 0
        height = [0] * m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            area = self.largestRectangleArea(height)
            max_area = max(max_area, area)
        
        return max_area

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        return self.maximalAreaOfSubMatrixOfAll1(matrix, n, m)