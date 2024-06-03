class Solution {
public:
    int maxDepth(string s) {
        int max_depth = 0;
        int curr_depth = 0;
        for(int i = 0; i < s.size() ; i++){
            if(s[i] == '('){
              curr_depth++;
              max_depth = max(curr_depth , max_depth);
            } 
                
            else if(s[i] == ')'){
                curr_depth--;
            }
        }
        return max_depth;
    }
};