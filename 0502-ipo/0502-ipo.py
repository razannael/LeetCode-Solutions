class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], 
                                         capital: List[int]) -> int:

        heap = []
        projects = sorted(zip(capital, profits),
                                       key=lambda x: x[0], reverse=True)

        for _ in range(k):
            while projects and projects[-1][0] <= w:
                heappush(heap, -projects.pop()[1])

            if heap: w-= heappop(heap)

        return w