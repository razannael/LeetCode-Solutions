/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
       if(root==NULL)
       return NULL;
       
       if(root->val==p->val||root->val==q->val)
       return root;
       
       TreeNode * l1=lowestCommonAncestor(root->left,p,q);
       TreeNode * l2=lowestCommonAncestor(root->right,p,q);
       if(l1!=NULL && l2!=NULL)
       return root;
       if(l2!=NULL)
       return l2;
       else 
       return l1;
    }
};