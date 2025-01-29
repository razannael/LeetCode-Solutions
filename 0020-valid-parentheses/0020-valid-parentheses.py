class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_map = {'}':'{', ')':'(',']':'['}
        for c in s:
            if c in my_map.values():
                stack.append(c)
            elif c in my_map.keys():
                if not stack or my_map[c]!= stack.pop():
                    return False
        return not stack
