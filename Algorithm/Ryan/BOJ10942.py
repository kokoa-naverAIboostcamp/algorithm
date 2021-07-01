# 10942번: 팰린드롬?
# 방법 1
import sys
def solution():
    N=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    M=int(sys.stdin.readline())
    dp=[[0]*(N) for _ in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(i,N):
            if arr[i] == arr[j]:
                if i+1 > j-1:
                    dp[i][j] = 1
                elif dp[i+1][j-1] == 1:
                    dp[i][j] =1

    for _ in range(M):
        S,E=map(int,sys.stdin.readline().split())
        print(dp[S-1][E-1])
solution()

# 방법 2
import sys
sys.setrecursionlimit(10**9)
def is_palindrome(s,e):
    if dp[s][e] >=0:
        return dp[s][e]
    if s == e:
        dp[s][e] =1
        return dp[s][e]

    if arr[s] == arr[e]:
        if s+1 <= e-1:
            dp[s][e]=is_palindrome(s+1,e-1)
        else :
            dp[s][e] =1
    else:
        dp[s][e] = 0
    return dp[s][e]

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
dp=[[-1]*(N) for _ in range(N)]
for _ in range(M):
    S,E=map(int,sys.stdin.readline().split())
    print(is_palindrome(S-1,E-1))