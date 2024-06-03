class Solution {
public:
    bool isStrictlyPalindromic(int n) {
        bool res = base(n , 2);
        for(int i = 3; i <= n-2 ; i++){
           res = res && base(n , i);
        }
        return res;
    }

    bool base(int n , int b){
        string s ="";
        while(n >= 1){
            s += to_string(n%b);
            n/=b;
        }
        int left = 0;
        int right = s.length() - 1;
        while(left <= right){
            if(s[left] != s[right]) return false;
            left++;
            right--;
        }
        return true;
    }
};