class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(' and x == ')':
                    stack.pop(-1)
                elif stack[-1] == '{' and x == '}':
                    stack.pop(-1)
                elif stack[-1] == '[' and x == ']':
                    stack.pop(-1)
                else:
                    return False
            
        return len(stack) == 0