class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        while front < back:
            if s[front].isalnum():
                if s[back].isalnum():
                    if s[front].lower() == s[back].lower():
                        front += 1
                        back -= 1
                    else:
                        return False
                else:
                    back -= 1
            else:
                front += 1
        return True