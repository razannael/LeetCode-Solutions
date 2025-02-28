# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        ls = []
        def backtrack(node):
            if node.right==None and node.left==None and sum(ls)==targetSum:
                res.append(ls.copy())
                return
            if node.left:
                ls.append(node.left.val)
                backtrack(node.left)
                ls.pop()
            if node.right:
                ls.append(node.right.val)
                backtrack(node.right)
                ls.pop()
            return     
        ls.append(root.val)   
        backtrack(root)
        return res