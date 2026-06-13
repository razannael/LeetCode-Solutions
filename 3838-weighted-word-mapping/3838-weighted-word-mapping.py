class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join([chr(ord('a') + 25 - (sum(weights[ord(i)-ord('a')] for i in word) % 26)) for word in words])
