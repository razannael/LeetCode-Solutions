import numpy as np

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        freq = [0] * 1501
        for f, _ in items:
            freq[f] += 1
        arr = [(p, sum(freq[f::f])) for f, p in items if p <= budget]
        arr.sort(reverse=True)
        dp = np.zeros(budget + 1, dtype=np.int64)
        ar = np.arange(budget + 1, dtype=np.int64)
        best = 0
        for p, v in arr:
            m = budget - p + 1
            t = int((dp[:m] + (m - 1 - ar[:m]) // p).max()) + v
            if t > best:
                best = t
            dp[p:] = np.maximum(dp[p:], dp[:m] + v)
        return best