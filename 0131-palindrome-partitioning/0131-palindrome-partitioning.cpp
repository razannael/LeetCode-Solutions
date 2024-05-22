class Solution {
public:
    vector<vector<string>> res;

    bool isPalindrome(string s,int left,int right){
        while(left<=right){
        if(s[left++]!=s[right--]){
            return false;
        }
            }
        return true;
    }

    void solve(int ind,string s, vector<string> &ds){
        if(ind==s.size()){
            res.push_back(ds);return;
            }
        for(int i=ind;i<s.size();++i){
            if(isPalindrome(s,ind,i)){
                ds.push_back(s.substr(ind,i-ind+1));
                solve(i+1,s,ds);
                ds.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<string> ds;
        solve(0,s,ds);
        return res;
    }
};