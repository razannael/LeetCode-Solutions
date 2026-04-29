class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        

        prefix = [[0] * (len(grid) + 1)]

        for i in range(len(grid) + 1):
            prefix.append([0] * (len(grid) + 1))
        
        # print(prefix)

        for i in range(len(grid)):
            sm = 0
            for j in range(len(grid[0])):
                sm += grid[j][i]
                prefix[j + 1][i] = sm

        # print(prefix)

        @cache
        def dp(col, prev, flag):

            if col >= len(grid):
                return 0

            
            ans = 0 
            
            for i in range(0, len(grid) + 1):


                if prev > i:
                    sm = 0
                    sm = (prefix[prev][col] - prefix[i][col])
                    ans = max(ans, sm + dp(col + 1, i, True))
                elif i > prev and not flag and col > 0:
                    sm_prev = 0
                    # for r in range(prev, i):
                    # print(i, prev)
                    # print(prefix[i][col], prefix[prev][col])
                    sm_prev = (prefix[i][col - 1] - prefix[prev][col - 1])
                    ans = max(ans, sm_prev + dp(col + 1, i, False))
                else:
                    ans = max(ans, 0 + dp(col + 1, i, False))

            
            return ans 
        

        tmp = dp(0, 0, True)
        dp.cache_clear()
        return (tmp)