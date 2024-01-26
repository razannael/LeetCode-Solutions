class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        temp ={}
        def rec(a, b, c):
            if (a,b,c) in temp : return temp[(a , b , c)]
            if a <0 or b <0 or a >= m or b>= n : return 1
            if c == 0 : return 0
            res = 0
            for x , y in [(1,0),(-1,0),(0,1),(0,-1)]:
                res += rec(a+x , b+y, c-1)
            temp[(a, b, c)] = res
            return res
        return rec(startRow, startColumn, maxMove ) % (10 ** 9 +7)