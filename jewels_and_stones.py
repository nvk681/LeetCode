class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)
        stones = list(stones)
        total = 0 
        for i in stones:
            total += jewels.count(i)
        return total