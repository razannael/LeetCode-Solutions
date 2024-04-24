class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int,int> repeating;
        for(int num : nums){
            repeating[num]++;
            if(repeating[num] > 1){
                return num;
            }
        }
         return -1;
    }
};