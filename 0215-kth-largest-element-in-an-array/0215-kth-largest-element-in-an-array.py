class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in nums:
            heapq.heappush(minheap, i)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]