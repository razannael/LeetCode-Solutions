class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_depth = 0

        for char in s:
            if char == '(':
                count += 1

            max_depth = max(count, max_depth)

            if char == ')':
                count -= 1

        return max_depth