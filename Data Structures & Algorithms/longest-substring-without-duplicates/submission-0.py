class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 1

        already = set()

        l = 0
        r = 1

        already.add(s[l])

        while r < len(s):
            print(r, already)
            if s[r] in already:
                if s[l] in already:
                   already.remove(s[l])
                already.add(s[r])

                l += 1
                r += 1

            if r < len(s):

                already.add(s[r])

            if len(already) > output:
                output = len(already)

            r += 1

        return output
