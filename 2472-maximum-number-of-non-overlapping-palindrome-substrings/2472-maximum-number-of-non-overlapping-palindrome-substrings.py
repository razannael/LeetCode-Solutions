class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # dp[i] represents the max non-overlapping palindromes in s[0:i]
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Base case: carry over the best result from the previous index
            dp[i] = dp[i - 1]
            
            # Check if there is a valid palindrome of exactly length k
            if i >= k:
                sub = s[i - k : i]
                if sub == sub[::-1]:
                    dp[i] = max(dp[i], dp[i - k] + 1)
                    
            # Check if there is a valid palindrome of exactly length k + 1
            if i >= k + 1:
                sub = s[i - k - 1 : i]
                if sub == sub[::-1]:
                    dp[i] = max(dp[i], dp[i - k - 1] + 1)
                    
        return dp[n]