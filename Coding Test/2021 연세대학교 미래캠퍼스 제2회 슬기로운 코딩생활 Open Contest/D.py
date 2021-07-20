# 22116번: 창영이와 퇴근
import sys
from heapq import heappop,heappush
INF=sys.maxsize
def dijkstra():
    slope=[[INF]*N for _ in range(N)]
    pq=[]
    heappush(pq,(0,(0,0))) # cost,(x,y)
    slope[0][0] = 0

    while pq:
        cost,(x,y) = heappop(pq)

        if (x,y) == (N-1,N-1):
            return slope[x][y]

        if cost > slope[x][y]:
            continue

        for d in dir:
            nx,ny=x+d[0],y+d[1]
            if 0 <= nx < N and 0 <= ny < N:
                next_cost=max(cost,abs(route[nx][ny]-route[x][y]))
                if next_cost < slope[nx][ny]:
                    slope[nx][ny]=next_cost
                    heappush(pq,(next_cost,(nx,ny)))

    return slope[-1][-1]

N=int(sys.stdin.readline())
route=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dir=[(0,1),(0,-1),(1,0),(-1,0)]
print(dijkstra())