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
