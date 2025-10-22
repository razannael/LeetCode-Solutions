from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def subtreeSizes(node, parent):
            nonlocal sizes
            for child in adj[node]:
                if child == parent or child in visited:
                    continue
                sizes[node] += subtreeSizes(child, node)
            return sizes[node]

        def findCentroid(node, parent, root):
            for child in adj[node]:
                if child == parent or child in visited:
                    continue
                if sizes[child] > sizes[root] // 2:
                    return findCentroid(child, node, root)
            return node

        def findDistances(node, parent, depth, count):
            if depth > k:
                return
            if len(count) == depth - 1:
                count.append(1)
            else:
                count[depth - 1] += 1
            for child in adj[node]:
                if child == parent or child in visited:
                    continue
                findDistances(child, node, depth + 1, count)

        def countTarget(node, parent, depth, total, curr):
            if depth > k:
                return
            nonlocal result
            result[node] += total[min(k - depth, len(total) - 1)] - curr[min(k - depth, len(curr) - 1)]
            for child in adj[node]:
                if child == parent or child in visited:
                    continue
                countTarget(child, node, depth + 1, total, curr)

        def centroidDecomposition(node):
            nonlocal visited, result, sizes
            sizes = [1] * n
            subtreeSizes(node, -1)
            centroid = findCentroid(node, -1, node)
            visited.add(centroid)
            prefixes = {}
            maxlen = 1
            for child in adj[centroid]:
                if child in visited:
                    continue
                count = []
                findDistances(child, centroid, 1, count)
                prefixes[child] = [0]
                for i in range(len(count)):
                    prefixes[child].append(prefixes[child][-1] + count[i])
                maxlen = max(maxlen, len(prefixes[child]))
            total = [1] * maxlen
            for child in prefixes:
                for i in range(maxlen):
                    total[i] += prefixes[child][min(i, len(prefixes[child]) - 1)]
            result[centroid] += total[min(k, len(total) - 1)]
            for child in adj[centroid]:
                if child in visited:
                    continue
                countTarget(child, centroid, 1, total, prefixes[child])
            for child in adj[centroid]:
                if child in visited:
                    continue
                centroidDecomposition(child)

        k -= 1
        if k < 0:
            maxcount = 0
        else:
            adj = defaultdict(list)
            for edge in edges2:
                adj[edge[0]].append(edge[1])
                adj[edge[1]].append(edge[0])
            n = len(edges2) + 1
            sizes = []
            visited = set()
            result = [0] * n
            centroidDecomposition(0)
            maxcount = max(result)
        k += 1
        adj = defaultdict(list)
        for edge in edges1:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        n = len(edges1) + 1
        sizes = []
        visited = set()
        result = [maxcount] * n
        centroidDecomposition(0)
        return result