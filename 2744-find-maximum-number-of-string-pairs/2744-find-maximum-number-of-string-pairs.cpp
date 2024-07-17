class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        unordered_map<string, int> mp;
        int res = 0;
        for (const auto& word : words) {
            string rev = reverseString(word);
            if (mp[rev] > 0) {
                res++;
                mp[rev]--;
            } else {
                mp[word]++;
            }
        }
        return res;
    }

    string reverseString(const string& s) {
        string rev = s;
        int n = rev.size();
        for (int i = 0; i < n / 2; ++i) {
            char temp = rev[i];
            rev[i] = rev[n - i - 1];
            rev[n - i - 1] = temp;
        }
        return rev;
    }
};
