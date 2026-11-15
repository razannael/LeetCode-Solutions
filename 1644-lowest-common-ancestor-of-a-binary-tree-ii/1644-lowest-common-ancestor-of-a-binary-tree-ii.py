from typing import Optional

class Solution:
    # Time: O(n)
    # Auxiliary space: O(h), where h is the tree height.
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'Optional[TreeNode]':
        found = 0

        def dfs(node):
            nonlocal found

            if node is None:
                return None

            # Explore children even when node is p or q:
            # the other target might be a descendant.
            left = dfs(node.left)
            right = dfs(node.right)

            if node is p or node is q:
                found += 1
                return node

            # Targets were found in different child subtrees.
            if left is not None and right is not None:
                return node

            # Propagate the candidate from the nonempty side.
            return left if left is not None else right

        ans = dfs(root)
        return ans if found == 2 else None