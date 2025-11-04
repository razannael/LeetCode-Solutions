class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        temp = n
        numList = []
        while temp > 0:
            numList.insert(0, temp%10)
            temp //=10
        digits = len(numList)
        totalNum = 0
        res = 0
        # less than K digits
        for j in range(digits-1, 0, -1):
            res = 9
            for k in range(9, 9-j+1,-1):
                res *= k
            totalNum += res
        #K digits
        seen = {}
        for i in range(0,digits):
            leadingDigit = numList[i]
            remainingDigits = len(numList) - i - 1
            for j in range(1 if i==0 else 0, leadingDigit):
                if j in seen:
                    continue
                res = 1
                for k in range(9-i, 9-i-remainingDigits,-1):
                    res *= k
                totalNum += res
            if leadingDigit in seen:
                break
            seen[leadingDigit] = 1
        seen = {}
        for num in numList:
            if num in seen:
                return n-totalNum
            seen[num] = 1
        return n-totalNum - 1