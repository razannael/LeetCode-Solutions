class Solution {
public:
    string reverseWords(string s) {
        string res;
        string curr;
        for(auto c : s){
            if(c == ' '){
                if (!curr.empty()) {
                    res += revWord(curr);
                    curr = ""; 
                }
                res += c; 
            }else {
                curr += c;
            }
        }
        if (!curr.empty()) {
            res += revWord(curr); 
        }
        return res;
    }

    string revWord(string word){
        int l = 0;
        int r = word.size() - 1; 
        char temp;
        while(l < r){
            temp = word[l];
            word[l] = word[r];
            word[r] = temp;
            l++;
            r--;
        }
        return word;
    }
};
