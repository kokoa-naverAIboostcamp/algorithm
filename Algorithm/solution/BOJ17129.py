#네오
import sys
from collections import deque
import copy
input = sys.stdin.readline

n,m = map(int, input().split())
info_map = [[0] for _ in range(m)]
x = y = 0

for i in range(n):
    info_map[i] = list(map(int,list(input().strip())))  #그냥 input도 안되고 strip대신 [:-1]해도 안됨
    #무조건 이렇게 해야됨 -> 입력값이 올바르지 않은 듯
    for j in range(m): 
        if info_map[i][j] == 2:
            x = i
            y = j
            break

def bfs(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    visited = [[0 for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append((x,y,0)) #2의 위치에서 시작
    visited[x][y] = 1
    # food = '345'

    while q:
        x,y,d = q.popleft()

        if info_map[x][y] == 3 or info_map[x][y] == 4 or info_map[x][y] == 5:
        # if str(info_[x][y]) in food: #라이언의 꿀팁!!
            print('TAK')
            print(d)
            return 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1

            if 0<=nx<n and 0<=ny<m \
                and visited[nx][ny] != 1 and info_map[nx][ny] != 1:
                q.append((nx,ny,nd))
                visited[nx][ny] = 1

    print('NIE')
    return
                
bfs(x,y)
