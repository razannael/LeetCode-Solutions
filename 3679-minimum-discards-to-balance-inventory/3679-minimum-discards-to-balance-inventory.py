from collections import defaultdict, deque
from typing import List

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        kept = defaultdict(deque)
        discards = 0

        for day, t in enumerate(arrivals, 1):
            q = kept[t]
            left = day - w + 1

            while q and q[0] < left:
                q.popleft()

            if len(q) >= m:
                discards += 1
            else:
                q.append(day)
            
        return discards