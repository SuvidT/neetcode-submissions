class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestPrice = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l += 1
                r += 1
            elif prices[r] - prices[l] > bestPrice:
                bestPrice = prices[r] - prices[l]
                r += 1
            elif prices[r] - prices[l] >= 0:
                r += 1
        return bestPrice