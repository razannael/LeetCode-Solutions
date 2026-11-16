class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new_s=""
            for i in range(0,len(s),k):
                total=0
                for j in s[i:i+k]:
                    total+=int(j)
                new_s+=str(total)
            s=new_s
        return s