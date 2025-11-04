class Solution:
    def findLUSlength(self, S: List[str]) -> int:
    	C = collections.Counter(S)
    	S = sorted(C.keys(), key = len, reverse = True)
    	for i,s in enumerate(S):
    		if C[s] != 1: continue
    		b = True
    		for j in range(i):
    			I, c = -1, True
    			for i in s:
    				I = S[j].find(i,I+1)
    				if I == -1:
    					c = False
    					break
    			if c:
    				b = False
    				break
    		if b: return len(s)
    	return -1
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com