class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # best = best score difference from the current state
        best = prefix[n - 1]

        # We can choose any prefix ending at index >= 1
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i] - best)

        return best