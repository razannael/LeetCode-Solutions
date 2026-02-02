class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        BuyP = prices[0]
        pro = 0
        for p in prices:
            if p < BuyP:
                BuyP = p
            pro = max(pro, p - BuyP)
        return pro