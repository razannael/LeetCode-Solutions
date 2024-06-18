class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> set;
        for(auto c : sentence){
            set.insert(c);
        }
        return set.size()==26;
    }
};