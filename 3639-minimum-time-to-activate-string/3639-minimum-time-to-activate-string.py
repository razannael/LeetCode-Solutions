class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total = n * (n + 1) // 2
        if total < k:
            return -1

        def check(m):
            stars = set(order[:m+1])
            stars.add(n)
    
            active = total
            window = 0
            for i in range(n + 1):
                if i not in stars:
                    window += 1
                else:
                    active -= window * (window + 1) // 2
                    window = 0
                    
            return active >= k
            
        l, r = 0, len(order) - 1
        res = -1
        while l <= r:
            m = (l + r) // 2

            if check(m):
                res = m
                r = m - 1
            else:
                l = m + 1       
        return res