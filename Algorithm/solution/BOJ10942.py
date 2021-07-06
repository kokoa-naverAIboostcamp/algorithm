# 팰린드롬?

### 찰스 ###
import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

dp = [[0]*n for _ in range(n)]

# fill dp
for i in range(n):
        dp[i][i] = 1     # 길이가 1인 경우 palindrome 이 맞다(1)

for i in range(2, n+1):  # 길이가 2 ~ n 인 경우에 대해 (n+1 포함 x)
    for j in range(n-i+1):
        if nums[j] == nums[j+i-1]: # 맨 앞, 맨 뒤가 같은 숫자인 경우
            if i == 2:      # 길이가 2인경우, 두 숫자가 같으면 palindrome
                dp[j][j+i-1] = 1
            elif dp[j+1][j+i-2] == 1:  # 그 중간이 palindrome 인지 확인
                dp[j][j+i-1] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    s, e = s-1, e-1
    print(int(dp[s][e]))

