class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        min_length = float('inf')
        for i,card in enumerate(cards):
            if card in seen:
                min_length = min(min_length, i - seen[card] + 1)
            seen[card] = i
        return min_length if min_length != float('inf') else -1