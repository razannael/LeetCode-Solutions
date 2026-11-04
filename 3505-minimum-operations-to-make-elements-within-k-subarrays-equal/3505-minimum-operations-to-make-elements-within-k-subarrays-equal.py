from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = [None]*n
        upper = SortedList()
        lower = SortedList()
        su = sl = 0 
        for i, v in enumerate(nums): 
            if not upper or upper[0] <= v: 
                upper.add(v)
                su += v
            else: 
                lower.add(v)
                sl += v
            if i >= x: 
                vv = nums[i-x]
                if vv >= upper[0]: 
                    upper.remove(vv)
                    su -= vv
                else: 
                    lower.remove(vv)
                    sl -= vv
            while len(upper) > len(lower)+1: 
                v = upper[0]
                upper.remove(v)
                su -= v
                lower.add(v)
                sl += v
            while len(upper) < len(lower): 
                v = lower[-1]
                lower.remove(v)
                sl -= v
                upper.add(v)
                su += v
            if i >= x-1: vals[i-x+1] = su - sl - upper[0]*(len(upper)-len(lower))
    
        dp = [[inf]*(k+1) for _ in range(n+1)]
        for i in range(n, -1, -1): 
            dp[i][0] = 0
            for j in range(1, k+1): 
                if n-i >= j*x: 
                    dp[i][j] = min(dp[i+1][j], vals[i] + dp[i+x][j-1])
        return dp[0][k]