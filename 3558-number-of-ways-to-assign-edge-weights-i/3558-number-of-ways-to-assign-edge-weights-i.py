class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:


        hs = defaultdict(list)

        for i, j in edges:
            hs[i].append(j)
            hs[j].append(i)

        seen = set()
        mx = 0
        def dfs(node, parent, v):
            nonlocal mx

            mx = max(mx, v)

            for n in hs[node]:
                if n != parent:
                    dfs(n, node, v + 1)
        
            return 
        
        (dfs(1, None, 0))

        return (pow(2, mx - 1, 10 ** 9 + 7))