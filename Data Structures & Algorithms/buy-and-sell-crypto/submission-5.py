class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = None
        profit = 0
        
        for price in prices:
            if not lowest_price:
                lowest_price = price
            elif lowest_price > price:
                lowest_price = price
            elif profit < price-lowest_price:
                profit = price - lowest_price

        return profit