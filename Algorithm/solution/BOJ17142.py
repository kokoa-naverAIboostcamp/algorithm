### 무지 ###
# 방법 1
from itertools import combinations
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(lab, virus, N):
    q = deque()
    check_time = [[-1 for _ in range(N)] for _ in range(N)]  # 이동 시간 저장 map
    for v in virus:
        check_time[v[0]][v[1]] = 0
        q.append(v)

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if lab[nx][ny] != 1 and check_time[nx][ny] == -1:
                    check_time[nx][ny] = check_time[x][y] + 1
                    q.append((nx, ny))

    ret = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2 or lab[i][j] == 0:
                if check_time[i][j] == -1: return -1
                if lab[i][j] == 0:
                    ret = max(ret, check_time[i][j])

    return ret


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 모든 바이러스의 위치를 좌표로 입력
virus = [(i, j) for i in range(N) for j in range(N) if lab[i][j] == 2]

# 모든 virus에 대해 조합으로 M개의 바이러스 선택한 list
virus_coms = list(combinations(virus, M))

# 각각의 조합 list에 대해 bfs를 돌려서 최소 시간 갱신
ans = -1
for com in virus_coms:
    ret = bfs(lab, com, N)
    if ret == -1: continue
    if ans == -1 or ans > ret: ans = ret

print(ans)


######################################################################################################
######################################################################################################


# 방법 2 (라이언 설명을 토대로 방법 1에 적용)
from itertools import combinations
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(lab, virus, N, empty):
    global ans      # 현재 최소 시간과 비교를 위해 전역 변수 사용
    q = deque()
    check_time = [[-1 for _ in range(N)] for _ in range(N)]  # (NxN) 크기의 이동 시간 저장 리스트
    for v in virus:
        check_time[v[0]][v[1]] = 0     # check_time에서 초기 M개의 활성 바이러스들의 좌표를 0으로 초기화
        q.append(v)

    ret = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if empty == 0:      # 빈 칸('0')의 개수가 0이므로 모든 칸에 바이러스를 퍼뜨림
                return ret      # 따라서 현재 최종 시간을 반환
            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != 1 and check_time[nx][ny] == -1:
                    check_time[nx][ny] = check_time[x][y] + 1
                    if ans != -1 and check_time[nx][ny] >= ans: # 현재 상태에서 시간이 이미 이전 최소 시간을 초과
                        return ans
                    ret = max(ret, check_time[nx][ny])
                    q.append((nx, ny))
                    if lab[nx][ny] == 0: empty -= 1     # 현재 방문한 칸이 빈 칸이면 empty를 1 감소

    if empty != 0: ret = ans    # 빈 칸의 개수가 0이 아니면 답이 아니다.
    return ret


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 모든 바이러스의 위치를 좌표로 입력
virus = []          # 바이러스('2')의 좌표를 tuple로 저장하는 리스트
empty_cnt = 0       # 빈 칸('0')의 개수
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
        if lab[i][j] == 0:
            empty_cnt += 1

# 모든 virus에 대해 조합으로 M개의 바이러스 선택한 list
virus_coms = list(combinations(virus, M))

# 각각의 조합 list에 대해 bfs를 돌려서 최소 시간 갱신
ans = -1
for com in virus_coms:
    t = bfs(lab, com, N, empty_cnt)
    if t == -1: continue
    if ans == -1 or ans > t:
        ans = t

print(ans)
