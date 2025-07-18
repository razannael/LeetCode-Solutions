import heapq

class Solution:
    def minimumDifference(self, nums):
        n3 = len(nums)
        n = n3 // 3

        leftMin = [0] * n3
        rightMin = [0] * n3

        # Max heap for left part (invert numbers to simulate max-heap)
        maxHeap = []
        leftSum = 0
        for i in range(n3):
            heapq.heappush(maxHeap, -nums[i])
            leftSum += nums[i]
            if len(maxHeap) > n:
                leftSum += heapq.heappop(maxHeap)
            if i >= n - 1:
                leftMin[i] = leftSum

        # Min heap for right part
        minHeap = []
        rightSum = 0
        for i in range(n3 - 1, -1, -1):
            heapq.heappush(minHeap, nums[i])
            rightSum += nums[i]
            if len(minHeap) > n:
                rightSum -= heapq.heappop(minHeap)
            if i <= n3 - n:
                rightMin[i] = rightSum

        # Calculate minimum difference
        result = float('inf')
        for i in range(n - 1, n3 - n):
            result = min(result, leftMin[i] - rightMin[i + 1])

        return result