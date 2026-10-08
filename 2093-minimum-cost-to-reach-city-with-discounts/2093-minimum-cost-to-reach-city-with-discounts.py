class UnionFind:

    def __init__(self, N):
        self.count = N              
        self.parent = [i for i in range(N)]
        self.rank = [1] * N
        
        
    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p]) 
        return self.parent[p]

    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        if self.rank[prt] >= self.rank[qrt]: 
            self.parent[qrt] = prt
            self.rank[prt] += self.rank[qrt]
        else:
            self.parent[prt] = qrt
            self.rank[qrt] += self.rank[prt]
            
        self.count -= 1 
        return True 
	    

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        '''
        find all paths from 0 to N - 1 with

        given a path from 0 to N - 1, we want to halve up the discount largest highways

        im hoping not path reconstruction


        5, 2

        10, 4

        7, 8

        shortest path + dp

        '''
        N = n
        UF = UnionFind(n)

        lookup = defaultdict(list)
        for u, v, w in highways:
            lookup[u].append((v, w))
            lookup[v].append((u, w))
            UF.union(u, v)
        

        if UF.find(0) != UF.find(n - 1):
            return -1


        def shortest_path_calc(lookup):
            INF = 10 ** 20
            min_dist = [[INF] * (discounts + 1) for _ in range(N)]
            min_dist[0][discounts] = 0

            h = []
            heapq.heappush(h, (0, 0, discounts))

            while h:
  


                val, u, d = heapq.heappop(h)

                if min_dist[u][d] < val:
                    continue

                for v, w in lookup[u]:
                  
                    total_weight = w + val

                    if total_weight < min_dist[v][d]:
                        min_dist[v][d] = total_weight
                        
                        heapq.heappush(h, (total_weight, v, d))

                    if d > 0:
                        total_weight = w // 2 + val

                        if total_weight < min_dist[v][d - 1]:
                            min_dist[v][d - 1] = total_weight
                            heapq.heappush(h, (total_weight, v, d - 1))


            return min_dist



        min_dist = shortest_path_calc(lookup)
        
        best = 10 ** 20
        for i in range(discounts + 1):
            best = min(best, min_dist[n - 1][i])

        return best



        