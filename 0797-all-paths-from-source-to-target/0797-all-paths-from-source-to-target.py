class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        res = []
        stack = [(0, [0])]
        while stack:
            node, path = stack.pop()
            if node == target: res.append(path)
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))
        return res