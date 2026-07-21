class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def counter(s):
            result = {}
            for i in s:
                if i in result:
                    result[i] += 1
                else:
                    result[i] = 1
            return result
    
        def checkInList(result, s):
            for i in result:
                for j in i:
                    if j == s:
                        return True
            return False

        result = []

        for i in range(0, len(strs)):
            if checkInList(result, strs[i]):
                continue
            minList = []
            minList.append(strs[i])
            for j in range(i+1, len(strs)):
                if counter(strs[i]) == counter(strs[j]):
                    minList.append(strs[j])
            result.append(minList)

        return result