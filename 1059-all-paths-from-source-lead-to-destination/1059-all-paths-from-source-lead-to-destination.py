class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # if no outgoing edge, false
        # if cycle, false
        graph = [[] for _ in range(n)]
        visited = {}

        for e in edges:
            graph[e[0]].append(e[1])

        if len(graph[destination]) > 0:
            return False

        def dfs(node, dest, visited):
            if node == dest:
                return True
            if node in visited:
                return visited[node]
            visited[node] = False
            if len(graph[node]) == 0:
                return False
            for next_node in graph[node]:
                if not dfs(next_node, dest, visited):
                    return False
            visited[node] = True
            return visited[node]
        
        return dfs(source, destination, visited)