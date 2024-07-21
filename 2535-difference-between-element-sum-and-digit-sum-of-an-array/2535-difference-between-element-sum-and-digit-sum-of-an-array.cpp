class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
      int elesum=0;
        for(auto i:nums)
            elesum+=i;
        for(int i=0;i<nums.size();i++){
            while(nums[i]!=0){
                int temp=nums[i]%10;
                elesum-=temp;
                nums[i]/=10;
            }
        }
        return elesum;  
    }
};