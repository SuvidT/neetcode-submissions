class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ''

        for i in range(len(strs)):
            finalStr += strs[i] + ';:'

        finalStr = finalStr[0:len(finalStr)]
        return finalStr

    def decode(self, s: str) -> List[str]:
        finalList = []

        i = 0
        j = 0
        while i < len(s):
            if s[i] == ';' and s[i+1] == ':':
                finalList.append(s[j:i])
                j = i + 2
            i += 1
        return finalList