class Solution {
public:
    int removePalindromeSub(string s) {
        if(s.size() == 0) return 0;
        else if(isPal(s)) return 1;
        return 2;
    }
    bool isPal(string s){
        int l = 0;
        int r = s.size() - 1;
        while(l < r){
            if(s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
    }
};