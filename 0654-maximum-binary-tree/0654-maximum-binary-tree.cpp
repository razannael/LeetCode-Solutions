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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return res(nums , 0 , nums.size()-1);
    }
    TreeNode* res(vector<int>& nums , int start , int end){
        if (start > end) return NULL;
        int m = start;
        for(int i = m+1 ; i <= end ; i++){
            if(nums[i] > nums[m]) m = i;
        }
        TreeNode* root = new TreeNode(nums[m]);
        root->left = res(nums , start , m - 1);
        root->right = res(nums , m + 1 , end); 
        return root;
    }
};