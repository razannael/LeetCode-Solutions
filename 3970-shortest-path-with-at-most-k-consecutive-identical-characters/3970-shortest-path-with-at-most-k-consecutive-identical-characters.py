class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')

        # dist[node][cnt] = minimum cost to reach node
        # with cnt consecutive identical characters
        dist = [[INF] * (k + 1) for _ in range(n)]

        pq = [(0, 0, 1)]  # (cost, node, consecutive count)
        dist[0][1] = 0

        while pq:
            cost, u, cnt = heapq.heappop(pq)

            if cost != dist[u][cnt]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:

                if labels[u] == labels[v]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_cost
                    heapq.heappush(
                        pq, (new_cost, v, new_cnt)
                    )

        return -1