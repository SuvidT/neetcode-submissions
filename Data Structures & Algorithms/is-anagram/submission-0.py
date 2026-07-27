class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSetS = set()
        hashSetT = set()

        for letter in s:
            hashSetS.add(letter)
        for letter in t:
            hashSetT.add(letter)

        if hashSetS == hashSetT:
            return True
        else:
            return False