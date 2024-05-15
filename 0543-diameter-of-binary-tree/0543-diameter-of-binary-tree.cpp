/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
            int res = 0;
        impl(root, res);
        return res;
    }

    int impl(TreeNode* node, int& res) {
        if (!node) return 0;
        int left = impl(node->left, res);
        int right = impl(node->right, res);
        int diameter = left + right;
        res = max(diameter, res);
        return max(left, right) + 1;
    }
};