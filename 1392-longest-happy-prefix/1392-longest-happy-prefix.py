class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        n = len(s)
        lps = [0] * n
        l, i = 0, 1
        
        while i < n:
            if s[l] == s[i]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
                    
        return s[:lps[-1]]