class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        if len(a) > len(b):
            b = (len(a) - len(b))*'0' + b
        elif len(b) > len(a):
            a = (len(b) - len(a))*'0' + a
        i,j = len(a)-1, len(b)-1
        
        carry = False
        summation = ''

        while i > -1 and j > -1:
            if (a[i] == b[j] == '1') and carry:
                summation = '1' + summation
                carry = True

            elif (a[i] == b[j] == '1') or ((a[i] == '1' or b[j] == '1') and carry):
                summation = '0' + summation
                carry = True

            elif a[i] == '1' or b[j] == '1' or carry:
                summation = '1' + summation                
                carry = False
                            
            else:
                summation = '0' + summation
                carry = False

            i -= 1
            j -= 1
        if carry:
            summation = "1"+summation

        return summation