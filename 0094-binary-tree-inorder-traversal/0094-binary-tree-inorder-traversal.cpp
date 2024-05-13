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
    vector<int> inorderTraversal(TreeNode* root) {
        vector <int> res ;
        inorder(res , root);
        return res;
    }
    void inorder (vector<int>& res , TreeNode* root){
        if(!root) return;
        inorder(res , root->left);
        res.push_back(root->val);
        inorder(res , root->right);
    }
};