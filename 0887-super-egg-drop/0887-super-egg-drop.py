class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        return bisect_left(range(0,n), n, key = lambda drops : sum(comb(drops, x) for x in range(1,k+1)) )
                