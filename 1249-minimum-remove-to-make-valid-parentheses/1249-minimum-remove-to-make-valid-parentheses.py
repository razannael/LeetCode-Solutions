class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        # Add remaining unmatched opening parentheses to to_remove
        to_remove.update(stack)
        
        # Construct the resulting string excluding characters to be removed
        result = ''
        for i, char in enumerate(s):
            if i not in to_remove:
                result += char
        
        return result