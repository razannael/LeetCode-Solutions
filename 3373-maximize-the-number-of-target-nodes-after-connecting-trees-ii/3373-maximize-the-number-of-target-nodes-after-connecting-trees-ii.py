class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        
        def fn(edges): 
            n = len(edges)+1
            tree = [[] for _ in range(n)]
            for u, v in edges: 
                tree[u].append(v)
                tree[v].append(u)
            ans = [0]*n
            cand = 0
            stack = [(0, -1, 0)]
            while stack: 
                u, p, k = stack.pop()
                ans[u] = k
                if k % 2 == 0: cand += 1
                for v in tree[u]: 
                    if v != p: stack.append((v, u, k^1))
            stack = [(0, -1, 0)]
            for u in range(n): 
                if ans[u] % 2 == 0: ans[u] = cand 
                else: ans[u] = n - cand
            return ans 
        
        most = max(fn(edges2))
        return [x + most for x in fn(edges1)]