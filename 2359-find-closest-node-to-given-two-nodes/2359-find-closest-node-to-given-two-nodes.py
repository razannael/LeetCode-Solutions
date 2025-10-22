class Solution:
    def cdist(self, it, distArray, distArrayIndex, edges):
        rdist = 0 
        nodes = []
        while it != -1 and distArray[it][distArrayIndex] > rdist:
            distArray[it][distArrayIndex] = rdist
            nodes.append(it)
            it = edges[it]
            rdist += 1
        return nodes
            
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        INF = float('inf')
        dist = defaultdict(lambda: [INF,INF])
        mmin, ans = INF, INF
               
        n = self.cdist(node1, dist, 0, edges)
        n += self.cdist(node2, dist, 1, edges)
                
        for k in n:
            m = max(dist[k])
            if m != INF:
                if m < mmin: 
                    mmin = m
                    ans = k
                elif m == mmin: 
                    ans = min(ans, k)
                    
        return ans if ans != float('inf') else -1