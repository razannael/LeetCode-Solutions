class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        gb, gr = defaultdict(list), defaultdict(list)

        for f, t in redEdges:
            gr[f].append(t)

        for f, t in blueEdges:
            gb[f].append(t)

        dq = deque()
        dq.append((0, 0, 0))
        dp = [[-1] * n, [-1] * n, [-1] * n]
        while dq:
            u, d, c = dq.popleft()

            if dp[c][u] == -1:
                dp[c][u] = d

                if c != 1:
                    for v in gb[u]:
                        # if dp[1][v] == math.inf:
                        dq.append((v, d + 1, 1))

                if c != 2:
                    for v in gr[u]:
                        # if dp[2][v] == math.inf:
                        dq.append((v, d + 1, 2))

        res = [min((dp[j][i] for j in range(3) if dp[j][i] != -1), default=-1) for i in range(n)]

        return res