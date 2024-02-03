class Solution:
 def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    n = len(arr)

    f = [0] * (n + 1)  # initialize the dynamic programming array
    for i in range(1, n + 1):  
        mx = 0  
        for j in range(
            1, min(i, k) + 1
        ):  
            mx = max(mx, arr[i - j])  
            f[i] = max(f[i], f[i - j] + mx * j) 
    return f[n]  
