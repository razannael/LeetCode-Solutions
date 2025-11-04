class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for i in num:
            n = n * 10 + i
        
        n = n + k
        num = []

        while n != 0:
            num.append(n % 10)
            n //= 10
            
        return num[::-1]