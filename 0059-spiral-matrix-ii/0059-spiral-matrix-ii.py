class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        
        def fill_circle(el, start, n):
            i, j = start, start            
            for k in range(j, j + n): 
                res[i][k], el = el, el + 1
            for k in range(i + 1, i + n): 
                res[k][j + n - 1], el = el, el + 1
            for k in reversed(range(j, j + n - 1)): 
                res[i + n - 1][k], el = el, el + 1
            for k in reversed(range(i + 1, i + n - 1)): 
                res[k][j], el = el, el + 1
        
        el, start = 1, 0
        while n > 0:
            fill_circle(el, start, n)
            el = el + 4*(n - 1)
            n, start = n - 2, start + 1
            
        return res