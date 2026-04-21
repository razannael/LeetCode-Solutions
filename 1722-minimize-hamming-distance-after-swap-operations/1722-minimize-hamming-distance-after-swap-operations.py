class UnionFind: 
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n
    
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p]) # path compression 
        return self.parent[p]
    
    def union(self, p, q): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False # already connected 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 
    

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind(len(source))
        for i, j in allowedSwaps: 
            uf.union(i, j)
        
        mp = {}
        for i in range(len(source)): 
            mp.setdefault(uf.find(i), []).append(i)
        
        ans = 0 
        for k, idx in mp.items(): 
            freq = {}
            for i in idx: 
                freq[source[i]] = freq.get(source[i], 0) + 1
                freq[target[i]] = freq.get(target[i], 0) - 1
            ans += sum(x for x in freq.values() if x > 0)
        return ans 