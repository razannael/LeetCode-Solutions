class Solution:
    def areSimilar(self, g: List[List[int]], k: int) -> bool:
        return [r[k%len(r):]+r[:k%len(r)] for r in g]==g