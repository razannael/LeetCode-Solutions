class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def fn(x):
            """Return next k-symmetric number."""
            n = len(x)//2
            for i in range(n, len(x)): 
                if int(x[i])+1 < k: 
                    x[i] = x[~i] = str(int(x[i])+1)
                    for ii in range(n, i): x[ii] = x[~ii] = '0'
                    return x
            return ["1"] + ["0"]*(len(x)-1) + ["1"]
                
        x = ["0"]
        ans = 0
        for _ in range(n): 
            while True: 
                x = fn(x)
                val = int("".join(x), k)
                if str(val)[::-1] == str(val): break
            ans += val
        return ans 