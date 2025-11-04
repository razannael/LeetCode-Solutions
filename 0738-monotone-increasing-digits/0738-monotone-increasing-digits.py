class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:

        n = str(n)                                        # For example: n = 246621 --> "246621"
        N = len(n)

        for i in range(N-1):                              # find the first break in monotonicity
            if n[i] > n[i+1]: break                       #       Ex: "2466 21"
                                                          #                ^
        else: return int(n)                               # if no break, then n is a mono non-decr seq
        
        while i>0 and n[i]==n[i-1]: i-=1                  # back up to the last digit in the mono incr seq 
                                                          #       Ex: "246 621"
                                                          #               ^
        return int(str(int(n[:i+1])-1)+'9'*(N-i-1))       # borrow a 1 from the mono incr portion and pad with 9s
                                                          #       Ex: ("246"-"1")+ '9'*4 = "245999"--> 245999