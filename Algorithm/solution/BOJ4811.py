### 무지 ###
import sys

dp = [[0 for _ in range(31)] for _ in range(31)]
for w in range(1, 31):
    dp[0][w] = 1
    for h in range(1, 31):
        if h > w: break
        dp[h][w] = dp[h][w-1] + dp[h-1][w]

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    print(dp[N][N])