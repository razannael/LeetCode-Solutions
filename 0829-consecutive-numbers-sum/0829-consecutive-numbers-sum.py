class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        csum=0
        result=0
        for i in range(1,n+1):
            csum+=i-1
            if csum>=n:
                break
            if (n-csum)%i==0:
                result+=1
        return result