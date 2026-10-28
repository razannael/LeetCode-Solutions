from heapq import heappush, heappop
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sm = sum(target)
        heap = []

        for x in target:
            heappush(heap, -x)

        while -heap[0] > 1:
            mx = -heappop(heap)
            rest_sm = sm - mx

            if rest_sm == 1:
                return True

            if rest_sm == 0:
                return False

            prev_mx = mx % rest_sm
            if prev_mx == 0 or prev_mx >= mx:
                return False

            heappush(heap, -prev_mx)
            sm = rest_sm + prev_mx

        return True