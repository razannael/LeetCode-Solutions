class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        deg = {i: set() for i in range(1, n + 1)}

        for a, b in edges:
            deg[a].add(b)
            deg[b].add(a)

        odd = [node for node in deg if len(deg[node]) % 2 == 1]

        if len(odd) == 0:
            return True

        if len(odd) == 2:
            u, v = odd
            if v not in deg[u]:
                return True

            for x in range(1, n + 1):
                if x != u and x != v and x not in deg[u] and x not in deg[v]:
                    return True
            return False

        if len(odd) == 4:
            a, b, c, d = odd
            if b not in deg[a] and d not in deg[c]:
                return True
            if c not in deg[a] and d not in deg[b]:
                return True
            if d not in deg[a] and c not in deg[b]:
                return True

        return False