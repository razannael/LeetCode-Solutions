class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        unordered_map<int , int>mp;
        vector<int>res;
        for(auto i : nums){
            mp[i] = nums[i];
        }
        for(auto i : nums){
            res.push_back(mp[i]);
        }
        return res;
    }
};