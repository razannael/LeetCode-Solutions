class Solution:
    def numTrees(self, n: int) -> int:
        uniq_tree = [1] * (n + 1)
        
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += uniq_tree[root - 1] * uniq_tree[nodes - root]
            uniq_tree[nodes] = total
        
        return uniq_tree[n]