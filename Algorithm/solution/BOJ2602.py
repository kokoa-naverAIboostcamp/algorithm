# 2602번: 돌다리 건너기 (라이언)
scroll=' '+input()
bridge=[' '+input() for _ in range(2)]
size=len(bridge[0])
dp=[[[0]*size for _ in range(2)] for _ in range(len(scroll))]

# 처음에 초기화
for y in range(0,size):
    for x in range(2):
        dp[0][x][y]=1

for i in range(1,len(scroll)):
    for y in range(1,size):
        for x in range(2):
            across=not x
            # 두루마리에 있는 문자열일때
            if bridge[x][y] == scroll[i] :
                dp[i][x][y]=dp[i-1][across][y-1]+dp[i][x][y-1]
            else:
                dp[i][x][y]=dp[i][x][y-1]

print(dp[-1][0][-1]+dp[-1][1][-1])