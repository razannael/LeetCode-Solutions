class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> mapNums;
        for(int i = 0 ; i < nums.size() ; i++){
            if(mapNums.count(nums[i]) && i - mapNums[nums[i]] <= k ){
                    return true;
            }
            mapNums[nums[i]] = i;
        }
        return false;
    }
};