import collections  
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = collections.defaultdict(int)
        prefix_sums[0] = 1
        prefix_sum = 0
        res = 0
        for i in range(n):
            prefix_sum += nums[i]
            key = prefix_sum-k
            if prefix_sums[key]:
                res += prefix_sums[key]
            prefix_sums[prefix_sum] += 1
        return res 