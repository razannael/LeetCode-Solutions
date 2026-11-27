class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        buy, profit = float("inf"), 0
        for i in prices:
            buy = min(buy, i)
            profit = max(profit, i - buy)
        return profit