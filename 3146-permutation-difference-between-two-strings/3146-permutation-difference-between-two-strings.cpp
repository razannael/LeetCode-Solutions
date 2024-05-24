class Solution {
public:
    int findPermutationDifference(string s, string t) {
        map<char, int> my_map;
        for(int i = 0; i < s.size(); i++){
            my_map[s[i]] = i ;
        }
        int res = 0;
        for(int i = 0 ; i < t.size() ; i++){
            res += abs(i - my_map[t[i]]);
        }
        return res;
    }
};