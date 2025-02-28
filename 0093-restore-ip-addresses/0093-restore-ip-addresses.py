class Solution:
    def valid(self, temp: str) -> bool:
        if len(temp) > 3 or len(temp) == 0:
            return False
        if len(temp) > 1 and temp[0] == '0':
            return False
        if len(temp) and int(temp) > 255:
            return False
        return True

    def solve(self, ans, output, ind, s, dots):
        if dots == 3:
            if self.valid(s[ind:]):
                ans.append(output + s[ind:])
            return
        for i in range(ind, min(ind+3, len(s))):
            if self.valid(s[ind:i+1]):
                new_output = output + s[ind:i+1] + '.'
                self.solve(ans, new_output, i+1, s, dots+1)

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.solve(ans, "", 0, s, 0)
        return ans