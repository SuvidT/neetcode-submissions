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
        
        # check columns
        for i in range(9):
            numList = []
            for j in range(9):
                if board[i][j] != '.':
                    numList.append(board[i][j])
            if len(numList) != len(set(numList)):
                return False
        
        
        
        return True
