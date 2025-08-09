class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        s = bin(n)
        s = s[2:]
        c = s.count('1')

        if c != 1:
            return False
        
        return True
        