class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0
        changes = set()

        l = 0
        r = 1

        while r < len(s):

            if s[l] == s[r]:


                if output < r - l + 1:
                    output = r - l + 1
                r += 1
                continue

            if len(changes) < k:
                changes.add(r)


                if output < r - l + 1:
                    output = r - l + 1
                r += 1
                continue

            if l in changes:
                changes.remove(l)

            l += 1


        return output
            