class Solution:
    def baseNeg2(self, n: int) -> str:
        res = ''   
        if n == 0  :   
            return  '0'
        while n != 0  :   
            result =  n % -2  
            if result  < 0 :   
                result +=  abs (-2)   
                n  =  n // -2 + 1  
            else :   
                n = n // -2  
            
            res =  str (result) + res  
        return res 