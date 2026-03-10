class Solution:
    def numberOfStableArrays(self, zero: int, one: int,limit: int) -> int:

        #def print_dp(): 
        #   print('idx0 = ', idx0, '    idx1 = ', idx1)
        #   for x in dp: print(x)
        #   print()

        zero+= 1
        one += 1
        limit+= 1

        dp = [[[0, 0] for _ in range(one)] for _ in range(zero)]
        for idx0 in range(min(zero, limit)): dp[idx0][0] = [1,0]
        for idx1 in range(min(one , limit)): dp[0][idx1] = [0,1]

        #print_dp()

        for idx0, idx1 in product(range(1, zero), range(1, one)):
            
            dp[idx0][idx1] = [sum(dp[idx0-1][idx1]), sum(dp[idx0][idx1-1])]
            
            if idx0 >= limit: dp[idx0][idx1][0]-=  dp[idx0-limit][idx1][1]
            if idx1 >= limit: dp[idx0][idx1][1]-=  dp[idx0][idx1-limit][0]

            #print_dp()  
            
        return sum(dp[-1][-1]) %1_000_000_007