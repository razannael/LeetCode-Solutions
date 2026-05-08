class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        
        @cache 
        def fn(n, k): 
            """Return number of ways to rearrange n sticks to that k are visible."""
            if n == k: return 1
            if k == 0: return 0
            return ((n-1)*fn(n-1, k) + fn(n-1, k-1)) % 1_000_000_007
        
        return fn(n, k) 