class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        invalidchars = len(s)
        l = 0
        r = 1

        while (l-1) < len(s):
            print(s[l:r])
            if s[l:r] in dictionary:
                invalidchars -= r-l
                l = r
                r = l + 1
            elif r >= len(s):
                l += 1
                r = l + 1
            else:
                r += 1
        return invalidchars