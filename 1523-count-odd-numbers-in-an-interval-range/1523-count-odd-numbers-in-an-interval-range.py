class Solution:
    def countOdds(self, low, high) -> int:
        ret_val = ((high if high % 2 == 1 else high-1) - (low if low % 2 == 1 else low + 1)) // 2 + 1

        return ret_val