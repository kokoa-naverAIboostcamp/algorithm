# 22115번: 창영이와 커피
#방법 1
import sys
INF=100001
N,K=map(int,sys.stdin.readline().split())
C=[0]+list(map(int,sys.stdin.readline().split()))
dp=[[INF]*(K+1) for _ in range(N+1)]
dp[0][0]=0

for i in range(1,N+1):
    for amount in range(K+1):
        if C[i] > amount :
            dp[i][amount] = dp[i-1][amount]
        else:
            dp[i][amount] = min(dp[i-1][amount-C[i]]+1,dp[i-1][amount])
print(-1 if dp[-1][-1] == INF else dp[-1][-1])

# 방법 2
import sys
INF=100001
N,K=map(int,sys.stdin.readline().split())
C=[0]+list(map(int,sys.stdin.readline().split()))
dp=[INF]*(K+1)
dp[0]=0

for i in range(1,N+1):
    for amount in range(K,C[i]-1,-1):
        dp[amount] = min(dp[amount-C[i]]+1,dp[amount])
print(-1 if dp[-1] == INF else dp[-1])