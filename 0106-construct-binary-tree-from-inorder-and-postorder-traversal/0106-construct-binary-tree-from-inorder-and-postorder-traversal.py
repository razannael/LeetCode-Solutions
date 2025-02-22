# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_tree(inorder, postorder):
            if not inorder:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            index = inorder.index(root_val)
            root.right = build_tree(inorder[index + 1:], postorder)
            root.left = build_tree(inorder[:index], postorder)
            return root

        return build_tree(inorder, postorder)