class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        if max(arr)<= 0 : return 0      #             arr = [-5,4,7,-2]
        sm, ct, mx,  = sum(arr), 0, 0   #              sm = 4
                                        # arr.extend(arr) = [-5,4,7,-2,-5,4,7,-2]
        if k > 1: arr.extend(arr)       #   
                                        #    n = [-5, 2, 4, 6,-5, 2, 4, 6]
        for n in arr:                   #   ct = [ 0, 4,11, 9, 4, 8,15,13]
            ct = max(ct + n, 0)         #   mx = [ 0, 4,11,11,11,11,15,15]
            mx = max(mx, ct)            #   
                                        #   15 + (3-2)*4*(3 > 1)*(4 > 0)
                                        #   15 + 1*4 * True*True = 19 <-- return
        return (mx + (k-2) * sm * (k > 1) * (sm > 0)) % 1000000007