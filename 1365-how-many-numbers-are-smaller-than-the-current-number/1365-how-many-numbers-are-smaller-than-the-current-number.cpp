class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        unordered_map<int , int> mp;
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        for(int i = nums.size()-1 ; i >= 0 ; i--){
            mp[sortedNums[i]] = i;
        }
        for(int i = 0 ; i < nums.size() ; i++){
            nums[i] = mp[nums[i]];
        }
        return nums;
    }
};