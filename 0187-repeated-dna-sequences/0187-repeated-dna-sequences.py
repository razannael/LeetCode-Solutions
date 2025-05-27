class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, seen = set(), set()
        for i in range(len(s)-9):
            dna = s[i:i+10]
            if dna in seen:
                ans.add(dna)
            else:
                seen.add(dna)
        return list(ans)