# 2045번: 마방진(라이언)

from collections import deque
def find_complete_sum():
    for i in range(3):
        if row[i] == 0:
            return sum(magic_square[i])
        if col[i] == 0:
            return sum(T_magin_square[i])

    diag_sum, r_diag_sum = 0, 0
    for i in range(3):
        for j in range(3):
            if i==j:
                diag_sum+=magic_square[i][j]
            if i+j==2:
                r_diag_sum+=magic_square[i][j]
    if diag[0]==0:
        return diag_sum
    if diag[1]==0:
        return r_diag_sum

magic_square=[]
for _ in range(3):
    magic_square.append(list(map(int,input().split())))
T_magin_square=list(zip(*magic_square))

if magic_square[1][1] == 0:
    if magic_square[0][2] != 0 and magic_square[2][0] !=0:
        magic_square[1][1] = (magic_square[0][2]+magic_square[2][0])//2
    elif magic_square[0][0] != 0 and magic_square[2][2] !=0:
        magic_square[1][1] = (magic_square[0][0] + magic_square[2][2]) // 2

row,col,diag=[0,0,0],[0,0,0],[0,0]
candidate=deque()
for i in range(3):
    for j in range(3):
        if magic_square[i][j] == 0:
            candidate.appendleft((i,j))
            if i == j:
                diag[0]+=1
            if i+j ==2:
                diag[1]+=1
            row[i]+=1
            col[j]+=1

complete_sum=find_complete_sum()
while candidate:
    x,y = candidate.pop()
    if row[x] == 1:
        magic_square[x][y]= complete_sum-sum(magic_square[x])
        row[x]-=1
        col[y] -= 1
    elif col[y] == 1:
        magic_square[x][y] = complete_sum - sum(T_magin_square[y])
        row[x] -= 1
        col[y]-=1
    else:
        candidate.appendleft((x,y))

for p in magic_square:
    print(*p,sep=' ')