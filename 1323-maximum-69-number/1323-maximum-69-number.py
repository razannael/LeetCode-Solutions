class Solution:
    def maximum69Number (self, num: int) -> int:
        tens=  (1000, 100, 10, 1)
        for t in tens:
            r=num//t%10
            if r==6:
                return num+3*t
        return num
        