import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from collections import defaultdict


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        if not edges:
            return 0 if src1 == dest and src2 == dest else -1

        # Explicitly deduplicate: keep only the minimum weight for each (u, v) pair
        min_edge = {}
        for u, v, w in edges:
            if (u, v) not in min_edge or w < min_edge[(u, v)]:
                min_edge[(u, v)] = w

        u_raw, v_raw, w_raw = zip(*[(u, v, w) for (u, v), w in min_edge.items()])

        # Forward graph (original directions)
        forward_adj = csr_matrix((w_raw, (u_raw, v_raw)), shape=(n, n))

        # Backward graph (reversed directions, for dijkstra from dest)
        backward_adj = csr_matrix((w_raw, (v_raw, u_raw)), shape=(n, n))

        # Shortest paths from src1, src2 (forward), and dest (backward)
        d1 = dijkstra(forward_adj, directed=True, indices=src1)
        d2 = dijkstra(forward_adj, directed=True, indices=src2)
        d_dest = dijkstra(backward_adj, directed=True, indices=dest)

        # Find node V minimizing d1[V] + d2[V] + d_dest[V]
        total_energy = d1 + d2 + d_dest
        min_weight = np.min(total_energy)

        return int(min_weight) if min_weight < np.inf else -1       