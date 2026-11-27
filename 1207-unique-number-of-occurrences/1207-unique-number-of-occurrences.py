from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        values=c.values()
        return len(set(values))==len(values)
        