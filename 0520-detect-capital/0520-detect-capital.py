class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        if word.isupper():
            return True
        if word==word.capitalize():
            return True
        return False
        
        