class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_set<int> seen;
        for(int num : nums){
            if(seen.count(num))
                seen.erase(num);
            else
                seen.insert(num);
        }
        return *seen.begin(); // The single number is the remaining element in the set
    }
};
