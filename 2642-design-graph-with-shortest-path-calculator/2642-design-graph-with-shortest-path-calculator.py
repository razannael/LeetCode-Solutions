class Graph:
    def __init__(self, n: int, edges: list[list[int]]):

        self.graph = defaultdict(list)
        for edge in edges: self.addEdge(edge)


    def addEdge(self, edge: list[int]) -> None:

        frm, to, edgeCost = edge
        self.graph[frm].append((to, edgeCost))


    def shortestPath(self, s: int, t: int) -> int:
        
        d, queue = defaultdict(lambda:-1, {s:0}), [(0,s)]
 
        while queue:
            a,b = heappop(queue)
            if d[b] == a:
                for to, edgeCost in self.graph[b]:
                    if d[to] > a + edgeCost or d[to] < 0:
                        d[to] = a + edgeCost
                        heappush(queue, (d[to], to))
        return d[t]