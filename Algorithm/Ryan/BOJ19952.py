#19952번: 인성 문제 있어??
import sys
from collections import deque
def bfs(F,start,end):
    q=deque()
    q.appendleft((start,F))  # ((x,y),F)
    visited[start[0]][start[1]]=1
    while q:
        (x,y),F=q.pop()
        for d in dir:
            nx,ny=x+d[0],y+d[1]
            if 0 <= nx < H and 0 <= ny < W:
                if F-1 >= 0 and visited[nx][ny] == 0 and maze[nx][ny]-maze[x][y] <= F:
                    if (nx,ny) == end:
                        return '잘했어!!'
                    q.appendleft(((nx,ny),F-1))
                    visited[nx][ny]=1
    return '인성 문제있어??'

dir=[(0,1),(0,-1),(1,0),(-1,0)]
T=int(sys.stdin.readline())
for _ in range(T):
    H,W,O,F,xs,yx,xe,ye=map(int,sys.stdin.readline().split())
    maze=[[0]*W for _ in range(H)]
    visited=[[0]*W for _ in range(H)]
    for _ in range(O):
        x,y,h=map(int,sys.stdin.readline().split())
        maze[x-1][y-1]=h
    print(bfs(F,(xs-1,yx-1),(xe-1,ye-1)))