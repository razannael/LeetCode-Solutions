class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        mult= len(b)//len(a)
        k= a*mult
        if b in k:
            return mult
        k= a*(mult+1) 
        if b in k:
            return mult+1
        k= a*(mult+2) 
        if b in k:
            return mult+2
        return -1