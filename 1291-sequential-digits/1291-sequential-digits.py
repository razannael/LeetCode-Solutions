# To solve this problem, we need to generate all the possible sequential digit
# numbers and check if they are within the range [low, high].
# One way to do this is to use a loop that starts from the smallest 
# possible sequential digit number, which is 12, and ends at the largest
# possible sequential digit number, which is 123456789. In each iteration,
# we can append the next digit to the current number and see if it is valid. 
# If it is, we can add it to the output list.
# If not, we can skip it and move on to the next number.



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
