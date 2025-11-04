class Solution:
    def kthGrammar(self, N: int, K: int) -> int:

        if N == 1:
            return 0
        
        parent = self.kthGrammar(N-1, math.ceil(K/2))
        is_odd = K % 2 == 1
        
        if parent == 1:
            return 1 if is_odd else 0
        else:
            return 0 if is_odd else 1