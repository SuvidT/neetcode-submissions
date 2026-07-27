class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack, token)
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
                continue

            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
                continue

            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
                continue

            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(a / b)
                continue

            num = ord(token) - ord('0')
            stack.append(num)

        return stack[0]