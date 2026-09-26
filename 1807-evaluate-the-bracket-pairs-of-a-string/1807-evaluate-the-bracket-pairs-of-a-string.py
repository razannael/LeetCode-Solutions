class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = {k: v for k, v in knowledge}
        ans = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                key = []
                while s[i] != ')':
                    key.append(s[i])
                    i += 1
                i += 1
                ans.append(mp.get("".join(key), "?"))
            else:
                ans.append(s[i])
                i += 1
        return "".join(ans)