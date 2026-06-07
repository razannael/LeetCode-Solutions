# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]: 
        node_dict = {}
        child_set = set()

        root = None

        for description in descriptions:
            val = description[0]
            if val in node_dict:
                tree = node_dict[val]
            else:
                tree = TreeNode(val)
                node_dict[val] = tree

            child_value = description[1]

            if child_value in node_dict:
                child_tree = node_dict[child_value]
            else:
                child_tree = TreeNode(child_value)
                node_dict[child_value] = child_tree

            child_set.add(child_tree)

            if description[2] == 1:
                tree.left = child_tree
            else:
                tree.right = child_tree

        for root_value, tree in node_dict.items():
            if tree not in child_set:
                return tree