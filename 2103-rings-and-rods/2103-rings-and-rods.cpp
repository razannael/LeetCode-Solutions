class Solution {
public:
    int countPoints(string rings) {
        unordered_map<int, unordered_set<char>> mp;
        int cnt = 0;
        for(int i = 1; i < rings.size(); i+=2){
            mp[rings[i]].insert(rings[i-1]);
        }
        for(auto it = mp.begin(); it != mp.end(); it++){
            if((it->second).size() == 3) cnt++;
        }
        return cnt;
    }
};