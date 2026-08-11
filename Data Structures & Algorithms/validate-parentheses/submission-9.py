class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        matching = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching:
                # If it's a closing bracket, verify the stack isn't empty 
                # and the top item matches the expected opening bracket
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                # If it's an opening bracket, push to stack
                stack.append(char)

        # Valid only if all opened brackets were matched and popped
        return not stack