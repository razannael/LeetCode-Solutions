class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## RC ##
		## APPROACH : SLIDING WINDOW ##
        # Logic #
        # 1. Increase the window if the substring is valid else,
        # 2. slide the window with the same length. No need to shrink the window
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        freqDict = defaultdict(int)
        maxFreq = 0
        maxLength = 0
        start = end = 0
        while end < len(s):
            freqDict[s[end]] += 1
            
            # maxFreq may be invalid at some points, but this doesn't matter
            # maxFreq will only store the maxFreq reached till now
            maxFreq = max(maxFreq, freqDict[s[end]])
            
            # maintain the substring length and slide the window if the substring is invalid
            if ((end-start+1) - maxFreq) > k:
                freqDict[s[start]] -= 1
                start += 1
            else:
                maxLength = max(maxLength, end-start+1)
            end += 1
        return maxLength