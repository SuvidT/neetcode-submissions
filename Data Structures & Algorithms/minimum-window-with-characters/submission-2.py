class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def ceq(x, t):
            for v, c in t.items():
                if v not in x:
                    return False
                if x[v] < c:
                    return False

            return True


        from collections import Counter

        T = Counter(t)

        if len(s) < len(t):
            return ""

        min_str = None

        for l in range(len(s)):
            for r in range(l,len(s)):
                x = Counter(s[l:r+1])

                if ceq(x, T):
                    if not min_str:
                        min_str = s[l:r+1]
                        continue
                    
                    if len(min_str) > len(s[l:r+1]):
                        min_str = s[l:r+1]
                        continue

        if min_str == None:
            return ""
        else:
            return min_str

                