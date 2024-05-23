class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<int> cnt(1001, 0); // To handle nums[i] up to 1000
        return backtrack(nums, k, 0, cnt) - 1; // Subtract 1 to exclude the empty subset
    }
    int backtrack(vector<int>& nums, int k, int idx, vector<int>& cnt) 
    {
        if (idx == nums.size()) 
        {
            return 1; // Each subset including empty one
        }
        // Option to exclude nums[idx]
        int result = backtrack(nums, k, idx + 1, cnt);
        
        // Option to include nums[idx] if it's valid
        if (nums[idx] - k >= 0 && cnt[nums[idx] - k] > 0) {
            return result; // Can't include nums[idx], return current result
        }
        
        // Include nums[idx]
        cnt[nums[idx]]++;
        result += backtrack(nums, k, idx + 1, cnt);
        cnt[nums[idx]]--; // Backtrack
        
        return result;
    }
};