class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # 2D table padded with extra row and col to eliminate boundary checks
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        max_side = 0

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "1":
                    # Offset indices by +1 to use padding safely
                    dp[i + 1][j + 1] = 1 + min(
                        dp[i][j + 1],  # Up
                        dp[i + 1][j],  # Left
                        dp[i][j]       # Up-Left
                    )
                    max_side = max(max_side, dp[i + 1][j + 1])

        return max_side * max_side