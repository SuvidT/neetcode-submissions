class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            L = s[l].lower()
            R = s[r].lower()

            if L != R:
                return False

            l += 1
            r -= 1

        return  True

