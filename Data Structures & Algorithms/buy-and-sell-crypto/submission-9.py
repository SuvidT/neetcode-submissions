class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit < 0:
                l = r
                r += 1
            
            if profit > max_profit:
                max_profit = profit

            r += 1

        return max_profit