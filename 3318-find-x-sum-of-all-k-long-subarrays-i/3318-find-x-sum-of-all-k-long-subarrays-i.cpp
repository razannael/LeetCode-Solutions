class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            c = [[count, val] for val, count in Counter(nums[i : i + k]).items()]
            c = heapq.nlargest(x, c)
            res.append(sum(val * count for count, val in c))
        return res