
from functools import lru_cache
# class Solution:
def maximumScore(nums, multipliers) -> int:
    @lru_cache(2000)
    def dp(i, left):
        right = len(nums)-1-(i-left)
        if i == len(multipliers):
            return 0
        x1 = nums[left]*multipliers[i]+dp(i+1, left+1)
        x2 = nums[right]*multipliers[i]+dp(i+1, left)
        return max(x1 , x2)
    return dp(0,0)

print(maximumScore([1,2,3], [3,2,1]))
# print(maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))