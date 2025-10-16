class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        prefixOps = [1] + [0] * 17   # cumulative ops for full power-of-4 blocks

        def totalOps(x: int) -> int:
            if x == 0:
                return 0
            log4 = (x.bit_length() - 1) >> 1   # floor(log4(x))
            remainder = x - (1 << (log4 << 1)) # leftover numbers after last full block
            return prefixOps[log4] + remainder * (log4 + 1)

        # Precompute prefix sums of operations for full power-of-4 intervals
        for i in range(1, 18):
            prefixOps[i] = prefixOps[i-1] + 3 * i * (1 << (2*(i-1))) + 1

        result = 0
        for left, right in queries:
            result += (totalOps(right) - totalOps(left-1) + 1) >> 1

        return result

