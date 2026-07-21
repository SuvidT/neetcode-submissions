class Solution:
    def maxScore(self, s: str) -> int:
        mscore = 0
        for i in range(1, len(s)):
            ls = list(s[0:i])
            rs = list(s[i:])
            
            l_score = 0
            for l in ls:
                if l == '0':
                    l_score += 1
            
            r_score = 0
            for r in rs:
                if r == '1':
                    r_score += 1
            
            if mscore < r_score + l_score:
                mscore = r_score + l_score
 

        return mscore