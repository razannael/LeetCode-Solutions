class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        subs, bal, start = [], 0, 0
        for i, ch in enumerate(s):
            bal += 1 if ch == '1' else -1
            if bal == 0:
                mid = self.makeLargestSpecial(s[start + 1:i])
                subs.append('1' + mid + '0')
                start = i+1
        subs.sort(reverse = True)
        return ''.join(subs)