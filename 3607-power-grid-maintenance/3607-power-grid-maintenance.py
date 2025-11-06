class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)           # unionfind
        for x, y in connections:
            uf.union(x, y)
        roots = {}                  # create a minHeap for each root of grid
        for x in range(1, c+1):
            y = uf.find(x)          # uf.find(x) = the smallest ID in the current grid
            if y not in roots:
                roots[y] = []
            heapq.heappush(roots[y], x)     # push x into the minHeap indexed by uf.find(x)
        ans = []
        offline = set()             # mark nodes as offline
        for num, x in queries:
            if num == 1:            # for maintenance check
                if x not in offline:    # if x is online, return x for current query
                    ans.append(x)
                    continue
                cur = roots[uf.parent[x]]   # otherwise, find the minHeap indexed by uf.parent[x]
                while cur and cur[0] in offline:    # find the smallest online ID in current grid
                    heapq.heappop(cur)
                if cur:                 # if there is online ID, return it
                    ans.append(cur[0])
                else:                   # else, return -1
                    ans.append(-1)
            else:                   # x goes offline
                offline.add(x)
        return ans

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x < root_y:         # merge larger root into smaller root, to keep the smallest ID as root in the current grid
            self.parent[root_y] = root_x
        elif root_x > root_y:
            self.parent[root_x] = root_y