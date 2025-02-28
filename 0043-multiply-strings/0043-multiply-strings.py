class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for num in num1:
            n1 *= 10
            n1 += dic[num] 
        for num in num2:
            n2 *= 10
            n2 += dic[num] 
        
        dic = ['0','1','2','3','4','5','6','7','8','9']        
        product = n1 * n2
        result = ''
        while product:
            val = product % 10
            result += dic[val]
            product //= 10
        if result == '':
            return '0'
        return result[::-1]

        