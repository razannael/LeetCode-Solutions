

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for firstDigit in range(1,10):
            num = firstDigit
            for nextDigit in range(firstDigit +1 , 10):
                num = num * 10 + nextDigit
                if low <= num <= high:
                    ans.append(num)
                elif num> high:
                    break
        ans.sort()
        return ans
