class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []  # Stack to hold intermediate strings
        ans = ""  # String to build the current result

        for ch in s:
            if ch == '(':
                # Push the current string to the stack & start a new one
                stack.append(ans)
                ans = ""
            elif ch == ')':
                # Reverse the current string
                ans = ans[::-1]
                # Concatenate with the string on top of the stack
                ans = stack.pop() + ans
            else:
                # Append regular characters to the current string
                ans += ch

        return ans  # Return the final result