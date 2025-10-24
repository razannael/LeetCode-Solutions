class Solution:
    def robotWithString(self, s: str) -> str:
        ret, n = "", len(s)
        suffixMin = [None]*n
		
		# construct suffix minimum array
        for i in range(n-1, -1, -1):
            if i == n-1: suffixMin[i] = s[i]
            else: suffixMin[i] = min(s[i], suffixMin[i+1])
		
        t = []
        for i in range(n):
			# append character at current index i to string t
            t.append(s[i])
			
			# check whether the last character of string t is not larger than the suffix min at index i+1,
			# if so, it means we cannot find a smaller character from the characters on the right side of current index i,
			# and we should print out the last character of string t
            while t and (i == n-1 or t[-1] <= suffixMin[i+1]): ret += t.pop()
        return ret