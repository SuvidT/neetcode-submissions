class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'}': '{', ']': '[', ')': '('}
        stack = []

        for x in s:
            if x not in hashMap:
                stack.append(x)
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] != hashMap[x]:
                    return False
                else:
                    stack.pop(-1)
        return len(stack) == 0