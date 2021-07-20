# [2021 연세대학교 미래캠퍼스 제2회 슬기로운 코딩생활 Open Contest](https://www.acmicpc.net/contest/view/665)

> 전체적으로 비교적 중간 난이도의 문제들이 많이 나왔다.





### A. [창영이와 버스](https://www.acmicpc.net/problem/22113) (BOJ22113)

> 문제에 제시된 내용을 충실하게 구현하면 풀 수 있는 문제. 여러 접근 방법이 있을 수 있는데, 대표적인 방법은 다음과 같다.

- 인접행렬 adj를 저장한다.
- 2번째 줄의 M개의 버스 번호를 순서대로 Start, End 지점의 cost를 더해서 출력한다.

```python
import sys
N,M=map(int,sys.stdin.readline().split())
bus=list(map(int,sys.stdin.readline().split()))
adj=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

cost=0
start=bus[0]-1
for end in bus[1:]:
    cost+=adj[start][end-1]
    start=end-1
print(cost)
```



### B.[창영이와 점프](https://www.acmicpc.net/problem/22114) (BOJ22114)

> 다이나믹 프로그래밍이나 투포인터로 푸는 문제. O(N)의 시간 복잡도로 풀 수 있다.

- 주어진 K보다 작은 연속된 최대 개수를 찾는 문제와 같다.
- 이때, 한번은 K보다 큰 값을 넘을 수 있다는 조건을 잘 생각해서 풀어야 한다.
- s,e는 0,0으로 시작하여 L[i]가 주어진 K보다 작으면 e -> +1 아니면 점프의 조건을 판단한다.
- 점프가 가능한 경우 jump -> 0 이고 `점프했을 때의 위치`를 기억하고 e -> +1
- 점프가 불가능한 경우 s,e의 위치를 결정하고 s는 `점프했을 때의 위치 + 1`로 이동한다.

```python
import sys
class _jump:
    def __init__(self,cnt,pos):
        self.cnt=cnt
        self.pos=pos

N,K=map(int,sys.stdin.readline().split())
L=list(map(int,sys.stdin.readline().split()))

s,e,ans=0,0,0
jump=_jump(1,0)
while e < N-1 and s<=e:
    if L[e] <= K:
        e+=1
    else:
        if jump.cnt > 0:
            jump.cnt -= 1
            jump.pos = e
            e+=1
        else:
            ans=max(ans,e-s+1)
            jump.cnt=1
            s,e = jump.pos+1,e
            jump.pos=0
print(max(ans,e-s+1))
```



### C. [창영이와 커피](https://www.acmicpc.net/problem/22115) (BOJ22115)

> 전형적인 배낭 문제이다. 배낭 문제와 조금 다른 점은 정확한 값이 있을 때만 dp에 넣어야 한다.

- 다이나믹 프로그래밍방법으로 풀어야 하고 시간 복잡도는 O(N*K)로 풀 수 있다.
- 여기서 가장 주의 해야할 점은 K=0일 때, 마실 수 없는 것이 아니라서 -1값이 아니라 0을 출력해 주어야 한다.

```python
#방법 1
import sys
INF=100001
N,K=map(int,sys.stdin.readline().split())
C=[0]+list(map(int,sys.stdin.readline().split()))
dp=[[INF]*(K+1) for _ in range(N+1)]
dp[0][0]=0

for i in range(1,N+1):
    for amount in range(K+1):
        if C[i] > amount :
            dp[i][amount] = dp[i-1][amount]
        else:
            dp[i][amount] = min(dp[i-1][amount-C[i]]+1,dp[i-1][amount])
print(-1 if dp[-1][-1] == INF else dp[-1][-1])

# 방법 2
import sys
INF=100001
N,K=map(int,sys.stdin.readline().split())
C=[0]+list(map(int,sys.stdin.readline().split()))
dp=[INF]*(K+1)
dp[0]=0

for i in range(1,N+1):
    for amount in range(K,C[i]-1,-1):
        dp[amount] = min(dp[amount-C[i]]+1,dp[amount])
print(-1 if dp[-1] == INF else dp[-1])
```



### D. [창영이와 퇴근](https://www.acmicpc.net/problem/22116) (BOJ22116)

> 다익스트라를 이용한 문제. 여기서 조금 더 효율적인 방법을 위해서 heapq를 사용했다.

```python
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
```