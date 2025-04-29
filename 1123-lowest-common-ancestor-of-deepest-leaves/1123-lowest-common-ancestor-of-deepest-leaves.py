class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return (0, None)
            l_depth, l_lca = helper(node.left)
            r_depth, r_lca = helper(node.right)
            if l_depth == r_depth:
                return (l_depth + 1, node)
            elif l_depth > r_depth:
                return (l_depth + 1, l_lca)
            else:
                return (r_depth + 1, r_lca)

        return helper(root)[1]