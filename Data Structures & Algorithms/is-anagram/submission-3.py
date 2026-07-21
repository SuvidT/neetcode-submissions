class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for x in range(0, len(s)):
            letterIndex = -1

            for y in range(0, len(t)):
                if s[x] == t[y]:
                    letterIndex = y
            
            if letterIndex == -1:
                return False
            t = t[0:letterIndex] + t[letterIndex + 1:len(t)]
        return True
