mod = 12345

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        myMul = lambda x, y : (x*y) % mod

        arr = list(chain(*grid))                                    #  <-- flatten
         
        pref = list(accumulate(arr,       myMul, initial=1))        #
        suff = list(accumulate(arr[::-1], myMul, initial=1))[::-1]  #  <-- solve
        ans = [p*s %mod for p,s in zip(pref,suff[1:])]              #

        return list(zip(*[iter(ans)] * n))                          #  <-- fold back up