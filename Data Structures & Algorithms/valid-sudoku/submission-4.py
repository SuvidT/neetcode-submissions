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
                if board[j][i] != '.':
                    numList.append(board[j][i])
            if len(numList) != len(set(numList)):
                return False
        
        # check boxes
        # looping boxes
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                # looping box
                numList = []
                for a in range(3):
                    for b in range(3):
                        if board[x+a][y+b] != '.':
                            numList.append(board[x+a][y+b])
                if len(numList) != len(set(numList)):
                    return False
        
        return True
