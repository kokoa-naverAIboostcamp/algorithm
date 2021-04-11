### 찰스 ###

import sys
from collections import deque 

def bfs(i,j): # return population, size, union_xy
    d_r = [0,-1,0,1] ## [서, 북, 동, 남]
    d_c = [-1,0,1,0]

    q = deque()
    q.append([i,j])

    population, size = 0, 0     # 인구수, 연합의 크기를 저장하는 변수
    union_xy = []               # 연합국가의 좌표들을 저장하는 리스트

    while q:
        r, c = q.popleft()
        
        if visit[r][c] == 0:
            size += 1
            population += nations[r][c]
            union_xy.append([r,c])
            visit[r][c] = size

            for k in range(4):
                if doors[r][c] & 1<<k == 0:                 # bit 연산. [서, 북, 동, 남] 방향으로 벽이 없는 경우
                    if visit[r + d_r[k]][c + d_c[k]] == 0 : # 벽 없는 쪽 좌표를 방문하지 않은 경우
                        q.append([r + d_r[k], c + d_c[k]])

    return population, size, union_xy
    

n, l, r = map(int, input().split())
nations = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = 0
while True:
    # 국경 : bit mask 로 표시 ex) 서: 1, 북: 10, 동: 100, 남: 1000, 전부 다 막음 = 1111 = 15
    doors = [[15]*n for _ in range(n)]
    
    # 1. 국경 열기

    for i in range(n):  
        for j in range(n-1): # 두개씩 비교하므로 마지막은 생략
            if l <= abs(nations[i][j] - nations[i][j+1]) <= r:
                doors[i][j] -= 4    # 동쪽 국경 개방
                doors[i][j+1] -= 1  # 서쪽 국경 개방
        
    for j in range(n):  
        for i in range(n-1): 
            if l <= abs(nations[i][j] - nations[i+1][j]) <= r:
                doors[i][j] -= 8    # 남쪽 국경 개방
                doors[i+1][j] -= 2  # 북쪽 국경 개방

    flag = 0                    # 전부 15(국경이 개방되지 않는 경우) 이면 0 => 반복 그만
    for i in doors:
        for j in i:
            if j != 15: 
                flag = 1 # 하나라도 15 가 아니면 flag = 1 => 반복문 계속 반복
                break
    if flag == 0: break
    ans += 1

    # 2. 인구 이동하기 -> bfs
    
    visit = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                population, size, union_xy = bfs(i,j)
                
                for a,b in union_xy:
                    nations[a][b] = population//size

print(ans)


