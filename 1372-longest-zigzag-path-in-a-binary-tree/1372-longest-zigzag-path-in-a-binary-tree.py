# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(root, right, total):
            if not root:
                return total
            
            l = helper(root.left, False, total+1 if right else 1)
            r = helper(root.right, True, total+1 if not right else 1)

            return max(l,r)
        
        return helper(root, None, 0) - 1