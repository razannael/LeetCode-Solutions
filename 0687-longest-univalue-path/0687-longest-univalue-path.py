class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.postOrder(root)
        return self.res
    
    def postOrder(self, node):
        if not node: return 0
        l_val = r_val = b_val = 0
        l_val = self.postOrder(node.left)
        r_val = self.postOrder(node.right)
        
        if node.left and node.right and (node.val == node.left.val == node.right.val):
            self.res = max(self.res, l_val + r_val + 2)
            return (max(l_val, r_val) + 1)
            
        elif node.left and (node.val == node.left.val):
            l_val += 1
            self.res = max(self.res, l_val)
            return l_val
        elif node.right and (node.val == node.right.val):
            r_val += 1
            self.res = max(self.res, r_val)
            return r_val
        else:
            return 0