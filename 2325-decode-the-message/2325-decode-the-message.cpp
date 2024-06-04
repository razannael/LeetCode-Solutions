class Solution {
public:
    string decodeMessage(string key, string message) {
        unordered_map<char, char> mp;
        char a = 'a';
        for(auto c : key){
            if(c == ' ') continue;
            if(mp.find(c) == mp.end()) mp[c] = a++; 
        }
        string res;
        for(auto c : message){
            if(c == ' ') res.push_back(' ');
            else res.push_back(mp[c]);
        }
        return res;
    }
};