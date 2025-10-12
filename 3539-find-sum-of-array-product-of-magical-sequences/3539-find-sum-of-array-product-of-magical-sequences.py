MOD = 10**9 + 7

@cache
def fact(n):
    if n == 0:
        return 1
    return (fact(n-1) * n) % MOD

class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        
        @cache
        def f(mask, m, k, depth): # return: sum of prods
            if m == 0:
                if mask.bit_count() == k:
                    return 1
                return 0
            if depth == len(nums):
                return 0
            res = 0
            # pick 0
            res += f(mask>>1, m, k - (mask & 1), depth+1)
            # pick > 0
            for c in range(1, m+1):
                # pick `c` of `00001`
                nmask = mask + c
                nm = m - c
                nk = k - (nmask & 1)
                sp = f(nmask >> 1, nm, nk, depth+1)
                res += (fact(m) * pow(fact(m-c), -1, MOD) * pow(nums[depth], c, MOD) * sp * pow(fact(c), -1, MOD)) % MOD
            return res
        return f(0, M, K, 0) % MOD