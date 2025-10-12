class Solution:
    def triangleNumber(self, T: List[int]) -> int:
    	L, t, _ = len(T), 0, T.sort()
    	for i in range(L-2):
    		k = i + 2
    		for j in range(i+1,L-1):
    			M = T[i] + T[j] - 1
    			if M < T[j]: continue
    			k = bisect.bisect_right(T, M, k)
    			t += min(k, L) - (j + 1)
    	return t