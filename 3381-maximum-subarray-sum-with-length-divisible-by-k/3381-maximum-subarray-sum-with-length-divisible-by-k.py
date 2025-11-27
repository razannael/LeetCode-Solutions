class Solution:
    def maxSubarraySum(self, nums: List[int], k: int, ans = -inf) -> int:

        def find_best(idx: int, mx = 0, res = -inf )-> int:
             
            for i in range(idx, len(nums) - k + 1, k):

                if mx < 0: mx = 0
                mx+= pref[i+k] - pref[i]
                res = max(res, mx)

            return res
            

        pref = list(accumulate(nums, initial = 0))
        return max(map(find_best, range(k)))