class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(s) < len(t):
            return ""

        T = Counter(t)

        counts = {}
        
        l = 0
        while l < len(s) and s[l] not in T:
            l += 1
        
        r = l
        last = r

        while r < len(s):
            if s[r] in T:
                if s[r] in counts:
                    counts[s[r]] += 1
                else:
                     counts[s[r]] = 1

                if s[r] == s[l] and counts[s[r]] > T[s[r]]:
                    counts[s[l]] -= 1
                    while s[l] not in T:
                        l += 1
                last = r

        

            r += 1


        return s[l:last+1]