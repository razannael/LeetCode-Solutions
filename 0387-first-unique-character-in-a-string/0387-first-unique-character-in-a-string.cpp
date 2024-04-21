class Solution {
public:
    int firstUniqChar(string s) {
        unordered_set<char> unique;
        unordered_set<char> repeating;
        for(int i = 0; i < s.size() ; i++){
            if(repeating.count(s[i]))
                continue;
            else if(unique.count(s[i])){
                unique.erase(s[i]);
                repeating.insert(s[i]);
            }else{
                unique.insert(s[i]);
            }
        }
        for(int i = 0 ; i < s.size() ; i++){
            if(unique.count(s[i]))
                return i;
        }
        return -1;
    }
};