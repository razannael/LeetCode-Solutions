class Solution:
    def minCost(self, A: List[int], B: List[int]) -> int:
        from collections import Counter
        count = Counter(A) - Counter(B)
        count += Counter(B) - Counter(A)
        if any(v % 2 for v in count.values()): return -1

        extra = []
        min_val = min(A + B)
        for k, v in count.items():
            extra += [k] * (v // 2)
        extra.sort()
        return sum(min(x, 2 * min_val) for x in extra[:len(extra)//2])