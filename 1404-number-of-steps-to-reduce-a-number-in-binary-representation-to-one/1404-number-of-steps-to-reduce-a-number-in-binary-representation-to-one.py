class Solution:
    def numSteps(self, s: str) -> int:

        n, tally = int(s,2), 0
        
        while n != 1: 
            if n&1: n+= 1 
            else:   n>>= 1    
            tally+= 1
        
        return tally
        