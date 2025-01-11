class Solution {
public:
    bool canConstruct(string s, int k) {
        unordered_map<char, int> freq;
        int single = 0;

        // Count character frequencies
        for (auto c : s) {
            freq[c]++;
        }

        // Count odd frequencies
        for (auto &[c, count] : freq) {
            if (count % 2 == 1) {
                single++;
            }
        }

        // Check if k is in the valid range
        return k >= single && k <= s.size();
    }
};