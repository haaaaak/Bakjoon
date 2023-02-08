n = int(input())
dp = list(map(int, input().split()))

dp.sort(reverse=True)

print(dp[0]+dp[1])
