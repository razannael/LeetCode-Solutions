class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def solve(i=1, lst=[], k=k):
            if k == 0:
                result.append(lst[:])
                return

            if i > n:
                return

            # Pick
            lst.append(i)
            solve(i + 1, lst, k - 1)

            # Backtrack
            lst.pop()

            # Not pick
            solve(i + 1, lst, k)

        solve()
        return result