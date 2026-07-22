class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        count = Counter(s)
        print(count)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1