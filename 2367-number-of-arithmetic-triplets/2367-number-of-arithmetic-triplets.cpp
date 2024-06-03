class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        map<int, int> mp;
        int cnt = 0;
        for(int num : nums) mp[num]++;
        for(int i = 0 ; i < nums.size(); i++){
            if(mp[nums[i] + diff] && mp[nums[i] + 2*diff]) cnt++;
        }
        return cnt;
    }
};