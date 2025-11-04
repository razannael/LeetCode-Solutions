class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # allocate the space, not so efficient
        dp = [[0]*(len(piles)) for k in range(len(piles))]

        # initial conditions:
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        
        # make caution of the sequence of updating, from small-gap to huge-gap (controlled by d)
        for d in range(1, len(piles)):
            for i in range(len(piles) - d):
                dp[i][i+d] = max(piles[i] - dp[i+1][i+d], piles[i+d] - dp[i][i+d-1])

        print(dp)      
        if dp[0][-1] > 0:
            return True
        
        return False
        
        
        # 'return True'