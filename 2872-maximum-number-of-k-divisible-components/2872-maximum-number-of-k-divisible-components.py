class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        src = 0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        comp = 0
        visited = set()
        def dfs(root):
            nonlocal comp
            if root in visited:
                return 0
            visited.add(root)
            ans = values[root]
            for neigh in adj[root]:
                ans += dfs(neigh)
            if ans % k == 0:
                comp += 1
                return 0
            return ans % k
        dfs(src)
        return comp