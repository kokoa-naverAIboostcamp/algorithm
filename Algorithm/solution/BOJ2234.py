### 라이언 ###
from collections import deque
import sys

def tuple_sort(x,y):
    return (min(x,y),max(x,y))

def bfs(i,j):
    q=deque()
    q.appendleft((i,j))
    visit[i][j]=cnt
    ans=1
    while q :
        x,y=q.pop()
        for d,s in zip(dir,bin(castle[x][y])[2:].zfill(4)):
            nx, ny = x + d[0], y + d[1]
            if 0<= nx <m and 0<= ny <n:
                if s=='0':
                    if visit[nx][ny] == 0:
                        q.appendleft((nx, ny))
                        visit[nx][ny]=cnt
                        ans+=1
                elif visit[nx][ny]!=0 and visit[nx][ny]!=cnt :
                    connect.add(tuple_sort(cnt,visit[nx][ny]))
    return ans


n,m=map(int,sys.stdin.readline().split())
visit=[[0]*n for _ in range(m)]
dir=[(1,0),(0,1),(-1,0),(0,-1)] #남, 동, 북, 서
castle=[]
connect=set()
room={}

for _ in range(m):
    castle.append(list(map(int,sys.stdin.readline().split())))

cnt=0
large_room=float('-inf')
remove=float('-inf')

# 가장 큰방과 방의 개수
for i in range(m):
    for j in range(n):
        if visit[i][j]==0:
            cnt+=1
            room[cnt]=bfs(i,j)
            if large_room < room[cnt]:
                large_room=room[cnt]

# 벽 제거하여 가장 넓은 방
for x,y in connect:
    if remove < room[x]+room[y]:
        remove=room[x]+room[y]

print(cnt)
print(large_room)
print(remove)