class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        
        # If the total length of s1 and s2 is not equal to s3, it's impossible
        if len_s1 + len_s2 != len_s3:
            return False
        
        # Create a 2D DP array to store intermediate results
        dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        
        # Base case: empty strings can always interleave to form an empty string
        dp[0][0] = True
        
        # Fill the first row
        for j in range(1, len_s2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # Fill the first column
        for i in range(1, len_s1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # Fill the DP array
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                # Check if the current position in s3 can be formed by interleaving
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len_s1][len_s2]