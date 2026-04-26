class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        min_val = min(arr)
        x = (sum(arr) - n * min_val) / (n * (n-1) // 2)    # Calculate arithmetic progression
        if x % 1 != 0:                                     # Arithmetic Progression must be Natural
            return False
        
        arr_set = set(arr)
        for i in range(n):
            if (min_val + i * x) not in arr_set:           # Ensure every calculated value in the sequence exists in our set
                return False
        return True