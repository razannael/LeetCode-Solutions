class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l, windowSum, res = 0, 0, float('inf')
        min_till = [float('inf')] * len(arr)

        for r, num in enumerate(arr):
            windowSum += num

            while windowSum > target:
                windowSum -= arr[l]
                l += 1

            if windowSum == target:
                curLen = r - l + 1
                res = min(res, curLen + min_till[l - 1])
                min_till[r] = min(curLen, min_till[r - 1])
            else:
                min_till[r] = min_till[r - 1]

        return res if res < float('inf') else -1