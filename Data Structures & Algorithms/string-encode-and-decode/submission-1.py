class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ''

        for i in range(len(strs)):
            finalStr += strs[i] + ';:'

        finalStr = finalStr[0:len(finalStr)]
        return finalStr

    def decode(self, s: str) -> List[str]:
        indexes = []
        finalList = []
        s = ';:' + s

        for i in range(len(s)):
            if s[i] == ';' and s[i+1] == ":":
                indexes.append(i)

        for j in range(len(indexes)-1):
            finalList.append(s[indexes[j]+1+1:indexes[j+1]])
        
        return finalList