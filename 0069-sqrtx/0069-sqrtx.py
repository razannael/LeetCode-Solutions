class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l<= r:
            m = l + (r-l)//2
            if m>x//m:
                r = m -1
            elif m < x//m:
                l = m+1
            else:
                return m
        return r