class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        vector<string> res;
        unordered_map<char, int> maxFreq;
        for (auto word : words2) {
            unordered_map<char, int> charInWords2Freq;
            for (auto c : word) {
                charInWords2Freq[c]++;
                maxFreq[c] = max(charInWords2Freq[c], maxFreq[c]);
            }
        }
        for (int i = 0; i < words1.size(); i++) {
            unordered_map<char, int> charsInWordFerq;
            for (auto c : words1[i]) {
                charsInWordFerq[c]++;
            }
            bool accepted = true;
            for (auto [c, requiredFreq] : maxFreq) {
                if (charsInWordFerq[c] < requiredFreq) {
                    accepted = false;
                    break;
                }
            }
            if (accepted) {
                res.push_back(words1[i]);
            }
        }
        return res;
    }
};