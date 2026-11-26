class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        for stones in (19, 15, 11, 7, 3):

            if n >= stones: n-= stones
               
            else: return n >= stones//2 +1

        return True