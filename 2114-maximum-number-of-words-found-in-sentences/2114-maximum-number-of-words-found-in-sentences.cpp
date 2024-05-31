class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int max_s = 0;
        for(auto sentence : sentences){
            int word_count = 1;
            for(char c : sentence){
                if (c == ' ') word_count++;
            }
            max_s = max(max_s , word_count);
        }
        return max_s;
    }
};