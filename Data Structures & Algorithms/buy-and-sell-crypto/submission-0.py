class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0

        for i in range(len(prices)-1):
            bp = 0
            for j in range(i+1, len(prices)):
                bp = prices[j] - prices[i]
                if bp >= bestProfit:
                    bestProfit = prices[j] - prices[i]
        return bestProfit