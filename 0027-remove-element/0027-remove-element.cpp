class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count =nums.size();
        for (int i =0 ;i< count;i++){
            if (nums[i]==val){
                nums.erase(nums.begin() + i);
                count--;
                i--;
            }
        }
        return count;
    }
};