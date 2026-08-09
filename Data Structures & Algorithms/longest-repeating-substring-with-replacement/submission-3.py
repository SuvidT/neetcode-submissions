class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Algorithm:
        1) if it is same as left pointer, add to count, increment
        2) if it isn't same as left pointer, check k >= (r - l + 1) - maxf, if true, increment, else increment l
        3) if
        """
        res = 0

        count = {}
        maxf = 0
        have_maxf = True

        l = 0
        r = 0
        while r < len(s):
            if s[l] == s[r]:
                if s[r] not in count:
                    count[s[r]] = 1
                else:
                    count[s[r]] += 1

                if count[s[r]] > maxf:
                    maxf = count[s[r]]
                    have_maxf = True

                if res < (r - l + 1):
                    res = r - l + 1

                r += 1
                continue

            if have_maxf and k > ((r - l + 1) - maxf):
                if s[r] not in count:
                    count[s[r]] = 1
                else:
                    count[s[r]] += 1

                if count[s[r]] > maxf:
                    maxf = count[s[r]]
                    have_maxf = True

                if res < (r - l + 1):
                    res = r - l + 1

                r += 1
                continue

            count[s[l]] -= 1
            l += 1

        return res+1
