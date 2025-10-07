class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        if k == 0:
            return s
            
        pattern = '(' * k + ')' * k
        
        # In a loop, replace all occurrences of the pattern with an empty string
        # The loop continues as long as replacements are being made
        prev_len = -1
        while prev_len != len(s):
            prev_len = len(s)
            s = s.replace(pattern, '')
            
        return s