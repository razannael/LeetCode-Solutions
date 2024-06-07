class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int r = nums.size();
        for(int i = 0 ; i < r ; i++){
          nums.push_back(nums[i]);
        }
        return nums;
    }
};