class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in word and i.upper() in word and word.rindex(i) < word.index(i.upper()):
                c+=1
        return c