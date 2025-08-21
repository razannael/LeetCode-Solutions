class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h = [0] * n
        cnt = 0
        for i in range(m):
            for j in range(n):
                h[j] = h[j] + 1 if mat[i][j] else 0
            for j in range(n):
                mn, k = h[j], j
                while k >= 0 and mn:
                    mn = min(mn,h[k])
                    cnt += mn
                    k -= 1
        return cnt