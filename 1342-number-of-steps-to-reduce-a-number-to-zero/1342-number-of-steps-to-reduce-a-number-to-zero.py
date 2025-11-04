class Solution:
    def numberOfSteps(self, num: int) -> int:
        ct = 0
        while num != 0:
            num = num/2 if num%2 == 0 else num-1
            ct += 1
        return ct