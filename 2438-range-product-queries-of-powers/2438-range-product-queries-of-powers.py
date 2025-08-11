class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        power = []

        if n & 1:
            power.append(1)
        n >>= 1
        val = 1
        while n:
            val <<= 1  
            if n & 1:
                power.append(val)
            n >>= 1

        prefix = [1] * len(power)
        prefix[0] = power[0] % mod
        for i in range(1, len(power)):
            prefix[i] = (prefix[i-1] * power[i]) % mod

        res = []
        for i, j in queries:
            if i == 0:
                res.append(prefix[j] % mod)
            else:
                inv = pow(prefix[i-1], mod-2, mod)
                res.append((prefix[j] * inv) % mod)
        return res