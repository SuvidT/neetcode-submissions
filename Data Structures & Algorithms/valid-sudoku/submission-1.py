class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            numList = []
            for i in row:
                if i != '.':
                    numList.append(i)
            if len(numList) != len(set(numList)):
                return False
        
        
        
        return True
