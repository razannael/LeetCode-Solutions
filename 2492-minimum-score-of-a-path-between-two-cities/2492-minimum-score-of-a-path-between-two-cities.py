class Solution:
    def __init__(self):
        self.root = []
        self.rank = []
    
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def createUnion(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.root = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        minScore = float('inf')
        for road in roads:
            self.createUnion(road[0], road[1])
        for road in roads:
            root1 = self.find(1)
            rootX = self.find(road[0])
            rootY = self.find(road[1])
            if root1 == rootX == rootY:
                minScore = min(minScore, road[2])
        return minScore