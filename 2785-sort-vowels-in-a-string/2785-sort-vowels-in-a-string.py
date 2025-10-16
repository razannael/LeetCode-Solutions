class Solution:
    def sortVowels(self, s: str) -> str:
        vowel=[97,101,105,111,117,65,69,73,79,85]
        s=list(s)
        lis=[]
        ind=[]
        for i in range(len(s)):
            if ord(s[i]) in vowel:
                lis.append(ord(s[i]))
                ind.append(i)
        lis.sort()
        if len(lis)<2:
            
            return "".join(s)
        
        for i in range(len(ind)):
            s[ind[i]]=chr(lis[i])
                
            
            
        return "".join(s)