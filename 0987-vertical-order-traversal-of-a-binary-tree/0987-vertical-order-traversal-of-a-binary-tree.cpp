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
    vector<vector<int>> ans;
    void p(TreeNode* root);
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        p(root);
        return ans;
    }
};

void Solution::p(TreeNode* root) {
    if (root == NULL) return;

    map<int, map<int, multiset<int>>> nodes;
    
    queue<pair<TreeNode*, pair<int, int>>> q;
    
    q.push({root, {0, 0}});
    
    while (!q.empty()) {
        auto temp = q.front();
        q.pop();
        
        TreeNode* node = temp.first;
        int col = temp.second.first;
        int row = temp.second.second;

        nodes[col][row].insert(node->val);
        
        if (node->left) {
            q.push({node->left, {col - 1, row + 1}});
        }
        if (node->right) {
            q.push({node->right, {col + 1, row + 1}});
        }
    }

    for (auto& colEntry : nodes) {
        vector<int> colVals;
        for (auto& rowEntry : colEntry.second) {
            colVals.insert(colVals.end(), rowEntry.second.begin(), rowEntry.second.end());
        }
        ans.push_back(colVals);
    }
}