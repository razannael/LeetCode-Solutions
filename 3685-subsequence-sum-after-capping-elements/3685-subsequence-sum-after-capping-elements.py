class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        res = [False] * n
        pq = nums[:]
        heapq.heapify(pq)
        # Dynamic canReach array: only update, never reset
        canReach = [False] * (k + 1)
        canReach[0] = True
        for x in range(1, n + 1):
            # pop and process all unique values less than x
            while pq and pq[0] < x:
                v = heapq.heappop(pq)
                for s in range(k, v - 1, -1):
                    if canReach[s - v]:
                        canReach[s] = True
            if canReach[-1]:
                res[x - 1] = True
                continue
            if k % x == 0 and 1 <= k // x <= len(pq):
                res[x - 1] = True
                continue
            for s in range(k + 1):
                if not canReach[s]:
                    continue
                if (k - s) % x == 0:
                    m = (k - s) // x
                    if 1 <= m <= len(pq):  # enough x's to use
                        res[x - 1] = True
                        break
        return res