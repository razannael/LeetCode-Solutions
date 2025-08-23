class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m=len(grid), len(grid[0])
        A=[0]*n
        T=[0]*m
        def build_A_T():
            for i, row in enumerate(grid):
                for j, x in enumerate(row):
                    if x==0: continue
                    A[i]|=(1<<j)
                    T[j]|=(1<<i)

        def minRect(i0, iN, j0, jN):
            iMin, iMax, jMin, jMax=30, -1, 30, -1
            for i in range(i0, iN+1):
                row=A[i]
                mRow=(row>>j0)<<j0
                mRow&=((1<<(jN+1))-1)
                if mRow:
                    iMin=i 
                    break
            if iMin==30: return 10**8
            for i in range(iN, iMin-1, -1):
                row=A[i]
                mRow=(row>>j0)<<j0
                mRow&=((1<<(jN+1))-1)
                if mRow:
                    iMax=i 
                    break
            for j in range(j0, jN+1):
                col=T[j]
                mCol=(col>>i0)<<i0
                mCol&=((1<<(iN+1))-1)
                if mCol:
                    jMin=j 
                    break
            for j in range(jN, jMin-1, -1):
                col=T[j]
                mCol=(col>>i0)<<i0
                mCol&=((1<<(iN+1))-1)
                if mCol:
                    jMax=j 
                    break
            return (iMax-iMin+1)*(jMax-jMin+1)

        build_A_T()
        ans=(1<<32)

        for c1 in range(m-2):
            for c2 in range(c1+1, m-1):
                a=minRect(0, n-1, 0,c1)
                b=minRect(0, n-1, c1+1, c2)
                c=minRect(0, n-1, c2+1, m-1)
                ans=min(ans, a+b+c)
        for r1 in range(n-2):
            for r2 in range(r1+1, n-1):
                a=minRect(0, r1, 0, m-1)
                b=minRect(r1+1, r2, 0, m-1)
                c=minRect(r2+1, n-1, 0, m-1)
                ans=min(ans, a+b+c)
        for r in range(n-1):
            for c in range(m-1):
                top=minRect(0, r, 0, m-1)
                bl=minRect(r+1, n-1, 0, c)
                br=minRect(r+1, n-1, c+1, m-1)
                ans=min(ans, top+bl+br)

                bottom=minRect(r+1, n-1, 0, m-1)
                tl=minRect(0, r, 0, c)
                tr=minRect(0, r, c+1, m-1)
                ans=min(ans, bottom+tl+tr)

                left=minRect(0, n-1, 0, c)
                tr=minRect(0, r, c+1, m-1)
                br=minRect(r+1, n-1, c+1, m-1)
                ans=min(ans, left+tr+br)

                right=minRect(0, n-1, c+1, m-1)
                tl=minRect(0, r, 0, c)
                bl=minRect(r+1, n-1, 0, c)
                ans=min(ans, right+tl+bl)
        return ans
       