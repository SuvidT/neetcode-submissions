class Solution:
    def maxScore(self, s: str) -> int:
        mscore = 0

        r_score = 0
        for char in s:
            if char == '1':
                r_score += 1

        l_score = 0
        for char in s[:-1]:
            if char == '0':
                l_score += 1
            elif char == '1':
                r_score -= 1
            
            if mscore < l_score + r_score:
                mscore = l_score + r_score
        
        return mscore