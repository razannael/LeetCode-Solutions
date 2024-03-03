/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums == null || nums.length == 0) return null;
        int low = 0; int high = nums.length - 1;
        return sort(nums, low, high);
    }
    public static TreeNode sort(int[] nums, int low, int high){
        if(low > high) return null;
        int mid =  (low + high) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        if(low == high) return root;
        root.left = sort(nums, low, mid - 1);
        root.right = sort(nums, mid + 1, high);
        return root;
    }
}