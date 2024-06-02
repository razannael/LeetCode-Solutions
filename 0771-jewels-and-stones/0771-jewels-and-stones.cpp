class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        set<char> s;
        for(int i = 0 ; i< jewels.size() ; i++){
            s.insert(jewels[i]);
        }
        int cnt = 0;
        for(int i = 0 ; i< stones.size() ; i++){
            if(s.contains(stones[i])) cnt++;
        }
        return cnt;
    }
};