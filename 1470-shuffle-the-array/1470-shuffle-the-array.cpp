class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> res;
        int left = 0;
        int right = n;
        for(int i = 0 ; i < n; i++){
         res.push_back(nums[i]);
         res.push_back(nums[i + n]);
        }
        return res;
    }
};