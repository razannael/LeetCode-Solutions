class Solution:
    def isValid(self, s: str) -> bool:
        stk,mtch = [0], {")":"(", "]":"[", "}":"{"}
        for c in s:
            if   c in mtch.values():  stk.append(c)
            elif stk[-1] == mtch[c]:  stk.pop()
            else:                     return False
        return not stk.pop()
        