class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        
        wordsToCode = set()
        
        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - 97]
            
            wordsToCode.add(code)
        
        return len(wordsToCode)
