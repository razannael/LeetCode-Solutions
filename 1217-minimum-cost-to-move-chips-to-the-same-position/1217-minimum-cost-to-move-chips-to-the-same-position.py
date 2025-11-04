class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:    
        nOdd, nEven = 0, 0
        for i in chips:
            if i % 2 == 0:
                nEven += 1
            else:
                nOdd += 1
        return min(nEven, nOdd)