def maximumScore(nums, multipliers) -> int:
    n, m = len(nums), len(multipliers)
    dp = [[0]*(m+1) for _ in range(m+1)]
    for i in range(m-1, -1, -1):
        for left in range(i, -1, -1):
            right = n - 1 - (i-left)
            mult = multipliers[i]
            dp[i][left] = max(mult*nums[left] + dp[i+1]
                                [left+1], mult*nums[right] + dp[i+1][left])
    return dp[0][0]

print(maximumScore([1,2,3], [3,2,1]))
# print(maximumScore([-5,-3,-3,-2,7,1],  [-10,-5,3,4,6]))