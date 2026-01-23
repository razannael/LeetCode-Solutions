from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        val = nums[:]                # current values
        prev = [i - 1 for i in range(n)]
        nxt  = [i + 1 for i in range(n)]
        nxt[n - 1] = -1
        alive = [True] * n

        def drop(i, j):
            # assumes i and j are valid indices
            return 1 if val[i] > val[j] else 0

        # 1) count initial drops
        dropsCount = 0
        for i in range(n - 1):
            dropsCount += drop(i, i + 1)

        # already sorted
        if dropsCount == 0:
            return 0

        # 2) build heap of adjacent sums
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (val[i] + val[i + 1], i, i + 1))

        ops = 0

        while dropsCount > 0:
            pair_sum, i, j = heapq.heappop(heap)

            # 3) validate: both alive AND still adjacent
            if not alive[i] or not alive[j] or nxt[i] != j or prev[j] != i:
                continue
            # NEW: stale-sum check
            cur_sum = val[i] + val[j]
            if pair_sum != cur_sum:
                heapq.heappush(heap, (cur_sum, i, j))
                continue

            L = prev[i]   # left neighbor of i
            R = nxt[j]    # right neighbor of j (the node after j)

            # 4) remove old drops involving borders (L-i), (i-j), (j-R)
            # Only borders that exist matter.
            if L != -1:
                dropsCount -= drop(L, i)
            dropsCount -= drop(i, j)
            if R != -1:
                dropsCount -= drop(j, R)

            # 5) merge i and j into i
            val[i] = val[i] + val[j]
            alive[j] = False

            # 6) reconnect links removing j
            nxt[i] = R
            if R != -1:
                prev[R] = i

            # 7) add new drops for new borders (L-i), (i-R)
            if L != -1:
                dropsCount += drop(L, i)
            if R != -1:
                dropsCount += drop(i, R)

            # 8) push new adjacent pairs into heap (only those that changed)
            if L != -1:
                heapq.heappush(heap, (val[L] + val[i], L, i))
            if R != -1:
                heapq.heappush(heap, (val[i] + val[R], i, R))

            ops += 1

        return ops
