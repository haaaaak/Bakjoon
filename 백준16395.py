n, k = map(int, input().split())


dp = [[1 for i in range(n)] for _ in range(31)]

for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

e_time = time.time()

print(dp[n-1][k-1])
