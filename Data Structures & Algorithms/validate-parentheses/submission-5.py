class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(":
                stack.append("(")
            elif char == "{":
                stack.append("{")
            elif char == "[":
                stack.append("[")
            elif char == ")":
                if stack.pop(-1) != "(":
                    return False
            elif char == "}":
                if stack.pop(-1) != "{":
                    return False
            elif char == "]":
                if stack.pop(-1) != "[":
                    return False
        
        if 0 != len(stack):
            return False

        return True
                