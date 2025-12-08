class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        for i in range(1,n):
            for j in range(1+i,n):
                t = math.sqrt(i*i + j*j)
                if int(t) == t and t <= n:
                    result += 2
        return result