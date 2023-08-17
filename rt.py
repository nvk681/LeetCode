def findMaxPoint(N, K, A):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for k in range(1, K + 1):
            dp[i][k] = max(
                dp[i - 1][k - 1] + A[i - 1] * (K - k + 1),
                dp[i - 1][k]
            )

    return max(dp[N])

# Sample Input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Output
print(findMaxPoint(N, K, A))