class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        returnlist = []
    
        for query in queries:
            curr = query[1]
            pre = query[0]

            stack = []
            found = False

            while len(stack) < len(prerequisites):
                for p in prerequisites:
                    if p[1] == curr:
                        if p[0] == pre:
                            found = True
                            break
                        curr = p[0]
                        stack.append(p)
                        continue
                break

            returnlist.append(found)

        return returnlist



            