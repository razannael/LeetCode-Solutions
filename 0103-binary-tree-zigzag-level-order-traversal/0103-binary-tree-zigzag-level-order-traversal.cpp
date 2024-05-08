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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(!root) return res;
        int level = 0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            vector<int> vlevel;
            int l = q.size();
            for(int i =0 ; i < l ; i++){
              TreeNode*node = q.front();
              q.pop();
              if(node->left != NULL) q.push(node->left);
              if(node->right != NULL) q.push(node->right);
              vlevel.push_back(node->val);
            }
            if(level % 2 == 0) res.push_back(vlevel);
            else{
                reverse(vlevel.begin(), vlevel.end());
                res.push_back(vlevel);
            }
            level ++;
        }
        return res;
    }
};