class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        from pprint import pprint

        ROWS = len(matrix)
        COLS = len(matrix[0])

        best = 1
        memory = {}
        print(memory)
        print(best)

        for i in range(ROWS):
            for j in range(COLS):
                val = matrix[i][j]
                if val == "0":
                    continue

                sq = 1

                up = 0
                left = 0
                up_left = 0

                if (i-1, j) in memory:
                    up = memory[(i-1, j)]

                if (i, j-1) in memory:
                    left = memory[(i, j-1)]

                if (i-1, j-1) in memory:
                    up_left = memory[(i-1, j-1)]

                if up == up_left and up_left == left:
                    sq += up_left
                else:
                    sq += min(up, left, up_left)

                memory[(i, j)] = sq
                if best < (sq * sq):
                    best = sq * sq


        return best