class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for index in range(len(prices)):
            if prices[index] < min_price:
                min_price = prices[index]
            elif max_profit < prices[index] - min_price:
                max_profit = prices[index] - min_price
        return max_profit
                