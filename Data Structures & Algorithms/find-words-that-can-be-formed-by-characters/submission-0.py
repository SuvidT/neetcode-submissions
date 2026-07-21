class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import defaultdict

        charsDict = defaultdict(int)
        for char in chars:
            charsDict[char] += 1

        returnval = 0
        for word in words:
            charsDictCopy = charsDict.copy()

            returnchars = 0
            for char in word:
                if char in charsDictCopy:
                    if charsDictCopy[char] > 0:
                        returnchars += 1
                        charsDictCopy[char] -= 1

            if returnchars == len(word):
                returnval += returnchars

        return returnval