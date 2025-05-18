MOD = 1000000007
MX = 100001

class Solution:
    def __init__(self):
        self.primeFactors = [0] * MX
        self._precompute_prime_factors()

    def _precompute_prime_factors(self):
        for i in range(2, MX):
            if self.primeFactors[i] == 0:
                for j in range(i, MX, i):
                    self.primeFactors[j] += 1

    def maximumScore(self, nums, k):
        n = len(nums)
        left, right = [-1] * n, [n] * n
        stack = []

        for i in range(n):
            while stack and self.primeFactors[nums[stack[-1]]] < self.primeFactors[nums[i]]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        elements = sorted(((nums[i], left[i], right[i], i) for i in range(n)), reverse=True)

        ans = 1
        for v, l, r, i in elements:
            total = (i - l) * (r - i)
            if total >= k:
                ans = (ans * pow(v, k, MOD)) % MOD
                break
            ans = (ans * pow(v, total, MOD)) % MOD
            k -= total

        return ans