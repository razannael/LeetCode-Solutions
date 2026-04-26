class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        l, r = 0,0
        while left != right:
            if l < r:
                l += left
                left+=1
            else:
                r += right
                right-=1
        if l==r:
            return left
        return -1