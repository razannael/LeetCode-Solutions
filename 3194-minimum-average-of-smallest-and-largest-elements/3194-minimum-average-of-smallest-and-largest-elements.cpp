class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        int time = nums.size()/2;
        vector<double>avg;
        sort(nums.begin(),nums.end());
        int s = 0 ;
        int e = nums.size()-1;
        while(time>0 && s<=e){
            double d = double(nums[s]+nums[e])/2;
            avg.push_back(d);
            s=s+1;
            e=e-1;
            time = time-1;
        }
        sort(avg.begin(),avg.end());
        return avg[0];
    }
};