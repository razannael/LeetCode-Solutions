from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_count = Counter(str(n))
        for i in range(31):
            if Counter(str(1 << i)) == n_count:
                return True
        return False