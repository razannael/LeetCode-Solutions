# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        counter =0
        while stack:
            node , path = stack.pop()
            path ^= (1 << node.val)
            if not node.left and not node.right:
                if path & (path-1) ==0:
                    counter +=1
            if node.left:
                stack.append((node.left, path))
            if node.right:
                stack.append((node.right, path))
        return counter

                
