class Solution:
    def makeFancyString(self, s: str) -> str:
        s=list(s)
        len, i=0, 0
        prev='@'
        for c in s:
            if prev!=c: len=1
            else: len+=1
            if len<=2:
                s[i]=c
                i+=1
            prev=c
        return "".join(s[:i])