class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = set()
        stack = [(root, None)]
        while stack:
            node, prev = stack.pop()
            if node.right and node.right.val in seen: 
                if node == prev.left: prev.left = None
                if node == prev.right: prev.right = None
                return root 
            seen.add(node.val)
            if node.left: stack.append((node.left, node))
            if node.right: stack.append((node.right, node))