from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache
        def check_profit(i, bought):
            max_profit = 0
            if i == len(prices): return max_profit
            if bought:
                max_profit = max(max_profit, check_profit(i+1, False)  + prices[i])
            else:
                max_profit = max(max_profit, check_profit(i+1, True) - fee - prices[i])
            max_profit = max(max_profit, check_profit(i+1, bought))
            return max_profit
        
        return check_profit(0, False)