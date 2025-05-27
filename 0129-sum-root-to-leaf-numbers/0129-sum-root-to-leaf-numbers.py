# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def getresult(self, root, result, tempresult):
        if root is None:
            return
        tempresult = tempresult * 10 + root.val
        if root.left is None and root.right is None:
            result[0] += tempresult
            return
        self.getresult(root.left, result, tempresult)
        self.getresult(root.right, result, tempresult)

    def sumNumbers(self, root):
        result = [0]  # Using a list to hold the result as a mutable object
        tempresult = 0
        self.getresult(root, result, tempresult)
        return result[0]