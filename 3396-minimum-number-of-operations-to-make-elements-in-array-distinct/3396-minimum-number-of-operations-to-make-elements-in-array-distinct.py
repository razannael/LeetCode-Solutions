class Solution:
    def minimumOperations(self, a: List[int]) -> int:
        s = ''.join(map(chr,a))
        while s!=(s:=re.sub(r'(?s).*(.)(.*\1.*)',r'\2',s)): pass
        return ceil((len(a)-len(s))/3)