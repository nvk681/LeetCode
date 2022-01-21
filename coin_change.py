from functools import lru_cache

def coinChange(coins, amount: int) -> int:
        @lru_cache(None)
        def get_the_count(i,amount_left):
            if amount_left == 0:
                return 0
            iteration = 0
            count = 0
            min_count = float('inf')
            while i < len(coins) and iteration*coins[i] <= amount_left:
                count = iteration+get_the_count(i+1, (amount_left-iteration*coins[i]))
                iteration += 1
                min_count = count if count < min_count else min_count
            return min_count
        
        value = get_the_count(0, amount)
        if value == float('inf'):
            return -1
        else: 
            return value
        
print(coinChange([1,2,5], 11))