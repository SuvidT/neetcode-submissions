class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 1
        already = set()

        l = 0
        r = 1

        already.add(s[l])


        while r < len(s):
            if s[r] in already:
                while l < r and s[l] in already:
                    l += 1

            already.add(s[r])
                
            if output < r - l + 1:
                output = r - l + 1

            r += 1

        return output