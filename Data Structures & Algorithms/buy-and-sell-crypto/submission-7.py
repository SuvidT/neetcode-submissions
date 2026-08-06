class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = None
        profit = 0
        
        for price in prices:
            
            if not lowest_price:
                lowest_price = price
                print(f"set lowest, proft: {profit}, lowest: {lowest_price}, curr: {price}")
            elif lowest_price > price:
                lowest_price = price
                print(f"reset lowest, proft: {profit}, lowest: {lowest_price}, curr: {price}")
            elif profit < price-lowest_price:
                profit = price - lowest_price
                print(f"set profit, proft: {profit}, lowest: {lowest_price}, curr: {price}")

        return profit