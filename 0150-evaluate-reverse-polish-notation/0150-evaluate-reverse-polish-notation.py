class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                # If the token is a number, push it onto the stack
                stack.append(int(token))
            else:
                # If the token is an operator, pop the last two operands from the stack
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Handle division with truncation toward zero
                    stack.append(int(a / b))

        return stack[0]

        