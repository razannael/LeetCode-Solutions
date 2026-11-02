class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

        graph = {}

        for e in edges:
            u, v, w = e

            if u not in graph:
                graph[u] = []
            graph[u].append([v, w])

            if v not in graph:
                graph[v] = []
            graph[v].append([u, w])

        for node in graph:
            adj = graph[node]

            for v, w in adj:
                dp[node][v] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        ans = -1
        min_count = float('inf')

        for i in range(n):
            count = 0

            for j in range(n):
                if i != j and dp[i][j] <= distanceThreshold:
                    count += 1

            if count <= min_count:
                min_count = count
                ans = i

        return ans