class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def find_parent(parent , node):
            if node == parent[node]:
                return node
            parent[node] = find_parent(parent , parent[node])
            return parent[node]
        
        def union(parent , rank , x , y):
            p1 = find_parent(parent , x)
            p2 = find_parent(parent , y)
            if p1 != p2:
                if rank[p1] == rank[p2]:
                    parent[p2] = p1
                    rank[p1] += 1
                elif rank[p1] < rank[p2]:
                    parent[p1] = p2
                else:
                    parent[p2] = p1

        def kruskal(edges , remove, force):
            rank   = [0 for i in range(n)]
            parent = [i for i in range(n)]
            heap = [ ( edges[i][2] , ( edges[i][0] , edges[i][1] ) , i ) for i in range(len(edges)) if remove == -1 or i != remove ]
            heapq.heapify(heap)
            total_weight = 0
            i = 0
            while(heap and i < n - 1):
                weight , edge , index = heapq.heappop(heap)
                x = edge[0]
                y = edge[1]
                if find_parent(parent , x) != find_parent(parent , y):
                    i += 1
                    total_weight += weight
                    union(parent , rank , x , y)
            
            if i != n - 1:
                return False
            
            forced_total_weight = 0
            if force != -1:
                rank   = [0 for i in range(n)]
                parent = [i for i in range(n)]
                heap = [ ( edges[i][2] , ( edges[i][0] , edges[i][1] ) , i ) for i in range(len(edges)) if force == -1 or i != force ]
                heapq.heapify(heap)
                i = 1
                union( parent , rank , edges[force][0] , edges[force][1] )
                forced_total_weight += edges[force][2]
                while(heap and i < n - 1):
                    weight , edge , index = heapq.heappop(heap)
                    x = edge[0]
                    y = edge[1]
                    if find_parent(parent , x) != find_parent(parent , y):
                        i += 1
                        forced_total_weight += weight
                        union(parent , rank , x , y)

            return [ total_weight , forced_total_weight ]
                

        withEdgeMSTWight , _ = kruskal(edges , -1, -1)
        critical = []
        pseudo_critical = []
        for i in range(len(edges)):
            thisEdgeMST = kruskal( edges , i , i )
            if thisEdgeMST:
                withoutEdgeMSTWeight , forcedEdgeMSTWeight = thisEdgeMST
                if withEdgeMSTWight < withoutEdgeMSTWeight:
                    critical.append(i)
                elif withEdgeMSTWight == forcedEdgeMSTWeight:
                    pseudo_critical.append(i)
            else:
                critical.append(i)
            
    
        return [ critical , pseudo_critical ]