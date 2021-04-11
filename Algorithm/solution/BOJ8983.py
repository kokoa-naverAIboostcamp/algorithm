### 무지 ###
import sys, bisect

# 이진탐색으로 얻은 사대에서 해당 동물을 사냥할 수 있는지 (사정거리:L)
def is_hunted(G, M, L, left, right, target_x, target_y):
    if left >= 0 and abs(G[left] - target_x) + target_y <= L:
        return True
    elif right < M and abs(G[right] - target_x) + target_y <= L:
        return True
    else:
        return False

M, N, L = map(int, sys.stdin.readline().split())
guns = list(map(int, sys.stdin.readline().split()))
guns.sort() # 입력 받은 사대를 오름차순 정렬

answer = 0
# N마리의 동물들의 좌표 입력 받기
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    idx = bisect.bisect(guns, x) # 이진 탐색으로 사대 리스트에서 동물의 x좌표의 바로 오른쪽 좌표를 구한다.
    if is_hunted(guns, M, L, idx-1, idx, x, y):
        answer += 1
print(answer)