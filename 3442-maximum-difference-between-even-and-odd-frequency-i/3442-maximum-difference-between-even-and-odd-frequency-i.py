from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        freq = Counter(s)
        min_even = float('inf')
        max_odd = float('-inf')

        for count in freq.values():
            if count % 2 == 0:
                min_even = min(min_even, count)
            else:
                max_odd = max(max_odd, count)

        return max_odd - min_even