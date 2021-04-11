### 무지 ###
## 풀이 1 - DFS를 이용한 풀이
import sys

# 주어진 출발 도시에서 dfs 수행 -> 이때, visited를 0으로 풀어줄 필요가 없다.
# 왜냐하면 왔던 도시를 중복 방문할 수 있기 때문에,
# 출발지에서 여행 계획에 속한 도시를 모두 방문한다면 무조건 순서대로 갈 수 있기 때문이다.
def dfs(cities, visited, current):
    visited[current] = 1
    for next, v in enumerate(cities[current]):
        if v == 0 or visited[next]: continue
        dfs(cities, visited, next)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
route = list(map(lambda x: x - 1, map(int, input().split())))
visited = [0] * N
dfs(cities, visited, route[0])

for city in route:
    if not visited[city]:
        print("NO")
        exit()
print("YES")


## 풀이 2 - 유니온 파인드 (참고: https://brenden.tistory.com/33)
import sys

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):   # x가 y 보다 작은 값
    x = find(x)
    y = find(y)
    # 부모가 같지 않은 경우
    if x != y:
        parent[y] = x

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [i for i in range(N)]
for i in range(N):
    cities = list(map(int, sys.stdin.readline().split()))
    for j in range(i, N):
        if cities[j]:
            union(i, j)

route = list(map(lambda x: x - 1, map(int, input().split())))
for i in range(M-1):
    if find(route[i]) != find(route[i+1]):
        print("NO")
        exit()
print("YES")

######################################################################################################
######################################################################################################

### 찰스 ###
## 풀이 1 - DFS를 이용한 풀이
import sys
from collections import defaultdict

n = int(input())                                # 도시 개수
m = int(input())                                # 방문 도시 개수
link = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] # 연결관계  이차원 list
plan = list(map(int, sys.stdin.readline().split()))                    # 방문계획  ex) plan = [1,2,3]

link_dic = defaultdict(list)                    # ex) link_dic = {0:[1], 1:[0,2], 2:[1]}
for i in range(n):
    for j in range(n):
        if link[i][j] == 1 : link_dic[i].append(j)


def DFS(link_dic):            # 완전탐색
    visit = [0]*n
    stack = []
    stack.append(plan[0]-1)   # plan (방문계획)에 있는 첫번째 도시에서 탐색시작
    while stack:
        current = stack.pop()
        visit[current] = 1
        for i in link_dic[current]:
            if visit[i] == 0 :
                stack.append(i)

    return visit

visit = DFS(link_dic)

ans = 'YES'
for i in plan:
    if visit[i-1] == 0:       # 방문 계획 도시중 하나라도 visit 에 없는 경우 ans = NO
        ans = 'NO'   
        break

print(ans)


### 찰스 ###
## 풀이 2 - 유니온 파인드           reference : https://ssungkang.tistory.com/entry/Algorithm-유니온-파인드Union-Find

import sys
from collections import defaultdict

n = int(input())                        # 도시 개수
m = int(input())                        # 방문 도시 개수
link = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] # 연결관계  이차원 list
plan = list(map(int, sys.stdin.readline().split()))

parent = [x for x in range(n)]          # parent[x] = x 로 초기화
rank = [1]*n                            # 각 노드의 트리 높이 

def find(parent,x):                     # x의 최상단 부모노드 (루트 노드) 를 찾는 함수
    if x == parent[x]: return x
    else : 
        y = find(parent,parent[x])
        parent[x] = y
        return y                        

def union(parent,x,y):                  # x,y 중 rank 가 더 높은 노드 밑에 낮은 노드를 연결해준다.   
    x = find(parent, x)                 # ex) x의 rank 가 더 높을 경우, y의 집합을 x의 집합에 합친다. (x가 y의 parent 가 된다.)
    y = find(parent, y)
    if x == y: return

    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]                


for i in range(n):
    for j in range(i+1, n):
        if link[i][j] == 1 : union(parent,i,j) # i, j 가 연결되어있는 경우 union() 으로 합친다.

ans = 'YES'

# find() 를 사용한 코드 - 오답
# check = find(parent,plan[0]-1)         # 방문 계획 도시중 첫번째 도시의 union 을 check 에 저장

# for i in plan:
#     if find(parent, i-1) != check:     # 방문 계획 도시중 하나라도 union 이 다르면 'NO'
#         ans = 'NO'   
#         break

# parent() 를 사용한 코드 - 정답 
check = parent[plan[0]-1]    # 방문 계획 도시중 첫번째 도시의 union 을 check 에 저장

for i in plan:
    if parent[i-1] != check:     # 방문 계획 도시중 하나라도 union 이 다르면 'NO'
        ans = 'NO'   
        break

print(ans)
