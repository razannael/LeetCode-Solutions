class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        count = 0
        equals = 0
        mpp = defaultdict(int)
        mpp[0] = 1
        for i in nums:
            if i % modulo == k:
                equals += 1
            rem = equals % modulo
            needed = (rem - k + modulo) % modulo
            count += mpp[needed]
            mpp[rem] += 1
        return count