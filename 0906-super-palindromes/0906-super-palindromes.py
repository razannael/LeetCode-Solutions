class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:

        def isPalindromic(s: str) -> bool:
            s = str(s)
            return s == s[::-1]

        def base3(n, s =''):
            while n:
                n, digit = divmod(n,3)
                s+= str(digit)
            return s[::-1]    

        cnt, left, right = left, isqrt(int(left)), isqrt(int(right))
        cnt = int(left <= 3 <= right)

        n = 0
        while True:
            n+= 1
            s = base3(n)

            evn, odd = int(s + s[::-1]), int(s + s[-2::-1])
            if evn < left : continue
            if odd > right: break
            
            if (evn <= right) and isPalindromic(evn * evn): cnt+= 1
            if (left <= odd ) and isPalindromic(odd * odd): cnt+= 1

        return cnt