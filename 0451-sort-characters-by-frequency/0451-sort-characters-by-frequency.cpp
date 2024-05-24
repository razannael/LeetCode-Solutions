#include<bits/stdc++.h>
class Solution {
public:
    string frequencySort(string s) {
        string ans;
        map<char,int>mpp;
        for(int i=0;i<s.size();i++){
            mpp[s[i]]++;
        }
        vector<pair<char,int>>temp;
        for(auto it:mpp){
            temp.push_back(make_pair(it.first,it.second));
        }
        sort(temp.begin(), temp.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;});
        for(auto it:temp){
            for(int i=0;i<it.second;i++){
                ans.insert(ans.begin()+0,it.first);
            }
        }
        return ans;

    }
};