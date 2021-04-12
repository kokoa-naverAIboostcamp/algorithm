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


# 4811번: 알약 (라이언)
import sys

dp=[[0 for j in range(31)] for i in range(31)]
for j in range(31):
    dp[0][j]=1
for i in range(1,31):
    for j in range(i,31):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]

while True:
    N=int(sys.stdin.readline())
    if N==0:
        break
    else:
        print(dp[N][N])