class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        @lru_cache(None)
        def dp(cntA: int, cntB: int, ans = 0)-> int:

            if cntA == 0: return 0
            if cntB == 0: return cntA <= limit
            
            maxA = min(cntA, limit)
            cntA-= 1

            for digitsA in range(maxA):
                ans+= dp(cntB, cntA - digitsA)

            return ans %1_000_000_007


        startZero = dp(zero, one)
        startOne  = dp(one, zero)

        return (startZero + startOne) %1_000_000_007
    