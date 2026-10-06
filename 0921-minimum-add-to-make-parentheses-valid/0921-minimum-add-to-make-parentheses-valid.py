class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = ans = 0

        for c in s:
            if c == '(':
                open += 1
            elif open:
                open -= 1
            else:
                ans += 1

        return ans + open