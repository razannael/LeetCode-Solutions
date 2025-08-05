class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:

        mx, ans = 0, 0

        for w in weight:
            if w < mx:          # <-- 1
                ans+= 1
                mx = 0

            else: mx = w        # <-- 2

        return ans    
        