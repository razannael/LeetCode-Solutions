class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        unordered_map <int, int> mp;
        for(int i:nums)
            mp[i]++;
        int count=0;
        for(int i:nums){
            if(mp.find(abs(i-k))!=mp.end())
                count+=mp[i-k];
            if(mp.find(i+k)!=mp.end())
                count+=mp[i+k];
        }
    return count/2;
    }
};