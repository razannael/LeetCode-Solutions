class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for(auto word : words){
            if(isPal(word)) return word;
        }
        return "";
    }

    bool isPal(string word){
        int l = 0;
        int r = word.size()-1;
        while(l <= r){
            if(word[l] != word[r]) return false;
            l++;
            r--;
        }
        return true;
    }
};