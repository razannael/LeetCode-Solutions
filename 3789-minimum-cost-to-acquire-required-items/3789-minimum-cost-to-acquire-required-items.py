class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        both = min(costBoth, cost1 + cost2)

        common = min(need1, need2)
        ans = common * both

        if need1 > need2:
            ans += (need1 - need2) * min(cost1, costBoth)
        else:
            ans += (need2 - need1) * min(cost2, costBoth)

        return ans