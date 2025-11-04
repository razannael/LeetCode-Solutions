class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        has2ndBitSet = bool(start & 2)
        end = start + 2*(n-1)
        k = (n - 1*has2ndBitSet) % 4

        # This reduce is O(1) time and space because k < 4 
        return (start*has2ndBitSet) ^ reduce(operator.xor, [end - 2*i for i in range(k)], 0)