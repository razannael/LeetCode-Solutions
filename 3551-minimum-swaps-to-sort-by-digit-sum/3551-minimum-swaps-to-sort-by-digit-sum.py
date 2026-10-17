class Pair:
    def __init__(self, d, val, idx):
        self.dsum = d
        self.val = val
        self.idx = idx

class Solution:
    def digitSum(self, num):
        return sum(int(d) for d in str(num))

    def minSwaps(self, nums):
        n = len(nums)
        pairs = [Pair(self.digitSum(nums[i]), nums[i], i) for i in range(n)]

        pairs.sort(key=lambda x: (x.dsum, x.val))

        i = 0
        cnt = 0
        while i < n:
            if pairs[i].idx != i:
                cnt += 1
                j = pairs[i].idx
                pairs[i], pairs[j] = pairs[j], pairs[i]
            else:
                i += 1
        return cnt