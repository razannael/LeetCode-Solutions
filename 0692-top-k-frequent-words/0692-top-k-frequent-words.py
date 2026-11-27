from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        counts = Counter(words)                                   # word → how many times it appears

        # heapq is a min-heap, so negative counts simulate a max-heap
        q = [(-value, key) for key, value in counts.items()]
        heapq.heapify(q)                                          # turn the list into a heap

        return [heapq.heappop(q)[1] for _ in range(k)]            # pop k times, keep only the word