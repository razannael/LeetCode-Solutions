class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num,count in freq.items():
            heapq.heappush(heap,(count,num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res
        