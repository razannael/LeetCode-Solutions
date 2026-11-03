class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        if n == 1:
            return n
        prev = ratings[0]
        streak = 1
        stack = 1
        d = 0
        lpeak = 0
        for i, num in enumerate(ratings):
            if num > prev:
                n += streak
                streak += 1
                stack = 1
                lpeak = streak
            elif lpeak > stack and num < prev:
                n += stack - 1
                stack += 1
                streak = 1
            elif lpeak == stack and num < prev:
                n += stack
                stack += 1
                streak = 1
            elif num < prev:
                n += stack
                stack += 1
                streak = 1
            else:
                streak = 1
                stack = 1
                lpeak = 0
            prev = num
        return n