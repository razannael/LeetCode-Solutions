class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for x in nums:
            x %= k
            cur = [0] * k

            # Start a new subarray
            cur[x] += 1

            # Extend previous subarrays
            for r in range(k):
                cur[r * x % k] += dp[r]

            dp = cur

            # Add current subarrays to the answer
            for r in range(k):
                ans[r] += dp[r]

        return ans