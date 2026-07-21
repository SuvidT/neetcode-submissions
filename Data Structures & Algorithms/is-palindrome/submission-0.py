class Solution:
    def isPalindrome(self, s: str) -> bool:
        alString = ''
        for i in s:
            if i.isalnum():
                alString += i.lower()
        
        newStr = ''
        for j in range(len(alString)-1, -1, -1):
            newStr += alString[j]

        return alString == newStr
