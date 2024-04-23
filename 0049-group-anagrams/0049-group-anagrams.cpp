class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash;
        string temp;
        for(string str : strs){
           temp = str;
           sort(str.begin(), str.end());
           hash[str].push_back(temp);
        }
        vector<vector<string>> res;
        for(auto itr = hash.begin() ; itr != hash.end() ; ++itr){
           res.push_back(itr->second);
        }
        return res;
    }
};