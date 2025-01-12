class Solution {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        if (n % 2 == 1) return false; // Odd-length strings cannot be valid
        
        stack<int> unLocked;
        stack<int> opens;
        
        for (int i = 0; i < n; i++) {
            if (locked[i] == '0') { // Compare to '0' instead of 0
                unLocked.push(i);
            } else if (s[i] == '(') {
                opens.push(i);
            } else { // The case where s[i] == ')'
                if (!opens.empty()) {
                    opens.pop();
                } else if (!unLocked.empty()) {
                    unLocked.pop();
                } else {
                    return false; // No way to balance this ')'
                }
            }
        }
        
        while (!opens.empty() && !unLocked.empty()) {
            if (unLocked.top() < opens.top()) {
                return false; // Unlocked '(' cannot come after locked ')'
            }
            opens.pop();
            unLocked.pop();
        }
        
        // If there are still unmatched '(' or unbalanced pairs, return false
        return opens.empty();
    }
};
