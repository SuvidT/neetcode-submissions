class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_box(i, j):
            if i < 3:
                if j < 3:
                    return 0
                elif j < 6:
                    return 1
                else:
                    return 2
            elif i < 6:
                if j < 3:
                    return 3
                elif j < 6:
                    return 4
                else:
                    return 5
            else:
                if j < 3:
                    return 6
                elif j < 6:
                    return 7
                else:
                    return 8
    

        rows = [set() for _ in board]
        cols = [set() for _ in board[0]]
        boxes = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):
                c = board[i][j]
                if c == ".":
                    continue
                val = int(c)

                if val > 9 or val < 1:
                    return False

                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                loc = get_box(i, j)
                if val in boxes[loc]:
                    return False
                boxes[loc].add(val)
        
        return True

                