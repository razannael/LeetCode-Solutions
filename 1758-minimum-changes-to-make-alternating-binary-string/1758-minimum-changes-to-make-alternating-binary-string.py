class Solution:
    def minOperations(self, s: str) -> int:
        answ1=answ0=0
        for i in range(len(s)):
            z=str(i%2)
            answ1+=s[i]!=z
            answ0+=s[i]==z
        return min(answ0,answ1)