import sys


n = int(sys.stdin.readline())
day = []
for i in range(n):
    day.append(list(map(int, sys.stdin.readline().split())))

dp = [0] * (n+1)

for i in range(n):
    if i + day[i][0] <= n:
        dp[i + day[i][0]] = max(dp[i + day[i][0]], dp[i] + day[i][1])
    dp[i + 1] = max(dp[i + 1], dp[i])
print(dp[n])
