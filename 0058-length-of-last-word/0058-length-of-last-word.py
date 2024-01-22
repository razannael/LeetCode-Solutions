class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = False
        last_word_length = 0
        for n in reversed(range(len(s))):
            if last_word == False and s[n] == ' ':
                continue
            last_word = True
            if s[n] != ' ':
                last_word_length +=1
            else:
                break
        return last_word_length
