class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int res =0;
        unordered_map<int,int> dp;
        for(int x : nums){
            res += dp[x]++;
        }
        return res;
    }
};