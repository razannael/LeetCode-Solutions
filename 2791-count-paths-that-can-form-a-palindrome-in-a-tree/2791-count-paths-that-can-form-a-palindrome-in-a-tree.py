class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        @cache
        def code(c):
            return 1<<(ord(c)-ord('a'))
        @cache
        def mask(i):
            if i==-1: return 0
            return mask(parent[i])^code(s[i])
        cnt=defaultdict(int)
        syms=set(s)
        ans=0
        for i in range(len(parent)):
            m=mask(i)
            ans += cnt[m]+sum(cnt[m^code(c)] for c in syms)
            cnt[m]+=1
        return ans
        