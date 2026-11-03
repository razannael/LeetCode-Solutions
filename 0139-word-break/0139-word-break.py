class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[-1]=True
        all=set(wordDict)
        maxi=max(map(len, wordDict))
        for i in range(len(s)):
            for j in range(max(0,i-maxi+1),i+1):
                word=s[j:i+1]
                if word in all and dp[j-1]==True:
                    dp[i]=True
        return dp[-2]