class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        res = 0
        interval = [0] * 1001  # Prefix count array

        for j in range(len(arr)):
            for k in range(j + 1, len(arr)):
                if abs(arr[j] - arr[k]) <= b:
                    left = max(0, max(arr[j] - a, arr[k] - c))
                    right = min(1000, min(arr[j] + a, arr[k] + c))
                    if left <= right:
                        if left == 0:
                            res += interval[right]
                        else:
                            res += interval[right] - interval[left - 1]
            for ind in range(arr[j], 1001):
                interval[ind] += 1

        return res