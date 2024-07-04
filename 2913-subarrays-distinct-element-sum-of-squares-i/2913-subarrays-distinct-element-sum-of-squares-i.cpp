class Solution {
public:
    int sumCounts(vector<int>& nums) {
        int result = 0;
        for (int i = 0; i < nums.size(); i++) {
            unordered_map<int, int> hash;
            for (int j = i; j < nums.size(); j++) {
                hash[nums[j]]++;
                result += (hash.size() * hash.size());
            }
        }
        return result;
    }
};