import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0

        pq = [(0, k)]  # (cost, node)

        while pq:
            cost, node = heapq.heappop(pq)

            if cost > dist[node]:
                continue

            for nei, w in graph[node]:
                new_cost = cost + w
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(pq, (new_cost, nei))

        ans = max(dist.values())
        return ans if ans < float('inf') else -1