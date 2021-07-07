# 21736번: 헌내기는 친구가 필요해
from collections import deque
def bfs(i,j):
    visited=[[0]*M for _ in range(N)]
    q=deque()
    q.appendleft((i,j))
    visited[i][j]=1
    res=0
    while q:
        x,y=q.pop()
        for d in dir:
            nx,ny=x+d[0],y+d[1]
            if 0<= nx < N and 0<= ny < M and visited[nx][ny] == 0:
                if campus[nx][ny] != 'X':
                    if campus[nx][ny] == 'P':
                        res+=1
                    q.appendleft((nx,ny))
                    visited[nx][ny]=1
    return res if res != 0 else 'TT'

def people_to_meet():
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                return bfs(i,j)

import sys
N,M=map(int,sys.stdin.readline().split())
campus=[sys.stdin.readline().strip() for _ in range(N)]
dir=[(0,1),(0,-1),(1,0),(-1,0)]
print(people_to_meet())