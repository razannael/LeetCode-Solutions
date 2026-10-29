class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # LCA preprocessing
        LOG = 17  # sufficient for n ≤ ~1e5
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(node: int, par: int):
            nonlocal timer
            tin[node] = timer
            timer += 1
            parent[0][node] = par

            for nei in graph[node]:
                if nei == par:
                    continue
                depth[nei] = depth[node] + 1
                dfs(nei, node)

            tout[node] = timer - 1

        dfs(0, -1)

        # Binary lifting table
        for k in range(1, LOG):
            for i in range(n):
                p = parent[k - 1][i]
                if p != -1:
                    parent[k][i] = parent[k - 1][p]

        def lca(u: int, v: int) -> int:
            """Lowest common ancestor via binary lifting."""
            if depth[u] < depth[v]:
                u, v = v, u

            # Lift u to same depth
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in reversed(range(LOG)):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        # Fenwick tree (XOR)
        size = n
        fenwick = [0] * (n + 1)

        def fenwick_add(i: int, val: int):
            i += 1
            while i <= size:
                fenwick[i] ^= val
                i += i & -i

        def fenwick_prefix(i: int) -> int:
            res = 0
            i += 1
            while i > 0:
                res ^= fenwick[i]
                i -= i & -i
            return res

        # Character mask
        def char_mask(c: str) -> int:
            return 1 << (ord(c) - ord('a'))

        labels = list(s)

        # Initialize Fenwick tree with subtree toggling
        for u, c in enumerate(labels):
            m = char_mask(c)
            fenwick_add(tin[u], m)
            fenwick_add(tout[u] + 1, m)

        # Process queries
        answers = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                delta = char_mask(labels[u]) ^ char_mask(new_char)
                labels[u] = new_char

                fenwick_add(tin[u], delta)
                fenwick_add(tout[u] + 1, delta)

            else:  # path query
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                path_mask = (
                    fenwick_prefix(tin[u])
                    ^ fenwick_prefix(tin[v])
                    ^ char_mask(labels[w])
                )

                # palindrome condition: ≤ 1 bit set
                answers.append(
                    path_mask == 0 or (path_mask & (path_mask - 1)) == 0
                )

        return answers