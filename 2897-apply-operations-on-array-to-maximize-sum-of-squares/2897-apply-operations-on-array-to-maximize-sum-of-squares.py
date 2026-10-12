class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 30

        for x in nums:
            for b in range(30):
                if x >> b & 1:
                    cnt[b] += 1

        ans = 0
        for _ in range(k):
            x = 0
            for b in range(30):
                if cnt[b]:
                    x |= 1 << b
                    cnt[b] -= 1
            ans = (ans + x * x) % MOD

        return ans