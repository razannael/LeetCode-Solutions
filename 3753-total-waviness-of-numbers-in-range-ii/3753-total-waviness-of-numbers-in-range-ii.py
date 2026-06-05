class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dfs(pos, tight, state, prev2, prev1):
                if pos == m:
                    return (1, 0)  # (count, total waviness)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if state == 0:
                        if d == 0:
                            cnt, wav = dfs(pos + 1, ntight, 0, 0, 0)
                        else:
                            cnt, wav = dfs(pos + 1, ntight, 1, d, d)

                        total_cnt += cnt
                        total_wavy += wav

                    elif state == 1:
                        cnt, wav = dfs(pos + 1, ntight, 2, prev1, d)

                        total_cnt += cnt
                        total_wavy += wav

                    else:  # state == 2 (at least two digits already)
                        add = 0
                        if (prev1 > prev2 and prev1 > d) or (
                            prev1 < prev2 and prev1 < d
                        ):
                            add = 1

                        cnt, wav = dfs(pos + 1, ntight, 2, prev1, d)

                        total_cnt += cnt
                        total_wavy += wav + cnt * add

                return (total_cnt, total_wavy)

            return dfs(0, True, 0, 0, 0)[1]

        return solve(num2) - solve(num1 - 1)