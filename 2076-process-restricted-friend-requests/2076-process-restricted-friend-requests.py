class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        res = []
        
        for u, v in requests:
            ru = dsu.find(u)
            rv = dsu.find(v)
            
            allowed = True
            
            if ru != rv:
                for x, y in restrictions:
                    rx = dsu.find(x)
                    ry = dsu.find(y)
                    
                    if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                        allowed = False
                        break
            
            res.append(allowed)
            
            if allowed:
                dsu.union(ru, rv)
        
        return res