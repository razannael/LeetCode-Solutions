from itertools import accumulate

class FenwickTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self._build(nums)

    def _build(self, nums):
        # Use prefix sums to initialize each node's responsibility window
        pre = [0] + list(accumulate(nums))
        for i in range(1, self.n + 1):
            self.tree[i] = pre[i] - pre[i - (i & -i)]

    def _increment(self, i, val):
        # Walk right, updating all nodes responsible for index i
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def _sum(self, i):
        # Walk left, accumulating prefix sum up to i
        s = 0
        while i >= 1:
            s += self.tree[i]
            i -= i & -i
        return s

    def sum_range(self, l, r):
        return self._sum(r) - self._sum(l - 1)

    def update(self, i, val):
        # Delta update: new_val - current_val
        self._increment(i, val - self.sum_range(i, i))


class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = FenwickTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index + 1, val)   # Convert to 1-indexed

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sum_range(left + 1, right + 1)  # Convert to 1-indexed