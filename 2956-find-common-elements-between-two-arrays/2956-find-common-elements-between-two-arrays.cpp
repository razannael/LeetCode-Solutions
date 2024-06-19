class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        vector<int> res;
        int cnt = 0;
        for(auto n : nums1){
            if(set2.find(n) != set2.end()){
                cnt++;
            }
        }
        res.push_back(cnt);
        cnt = 0;
        for(auto n : nums2){
            if(set1.find(n) != set1.end()){
                cnt++;
            }
        }
        res.push_back(cnt);
        return res;
    }
};