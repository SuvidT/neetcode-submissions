class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def counter(s: str) -> tuple:
            c = [0] * 26
            for x in s:
                c[ord('a') - ord(x)] += 1
            return tuple(c)

        seen = {}

        for i, s in enumerate(strs):
            c = counter(s)

            if c in seen:
                seen[c].append(s)
            else:
                seen[c] = [s]

        return list(seen.values())