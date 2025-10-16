class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        #
        A,B,i = 0,0,0
        
        if n < 10: return n-1,1
        
        while n >= 10:
            digit = n%10
            n = n//10
            if digit <= 1:
                A += (digit+1)*10**i
                B += 9*10**i
                n = n-1
            else:
                B += (digit-1)*10**i
                A += 1*10**i
            i += 1
        
        B += n*10**i
        
        return A,B