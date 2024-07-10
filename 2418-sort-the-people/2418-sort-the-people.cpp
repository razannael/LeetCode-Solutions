class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        map<int, string, greater<int>> mp; 
        vector<string> new_names;
        
        for (int i = 0; i < names.size(); i++) {
            mp[heights[i]] = names[i];
        }
        
        for (auto it = mp.begin(); it != mp.end(); ++it) {
            new_names.push_back(it->second);
        }
        
        return new_names;
    }
};
