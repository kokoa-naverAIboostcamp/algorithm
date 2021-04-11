#네오
import sys

N = int(sys.stdin.readline())
liq = list(map(int,sys.stdin.readline().split())) #이미 오름차순

left = 0 
right = N-1
rl = left 
rr = right
temp = liq[left] + liq[right] #초기값

while left < right: 
    res = liq[left] + liq[right] 
    if abs(temp) > abs(res): #0에 가장 가까운값 갱신 시
        temp = res
        rr = right
        rl = left

    if res < 0: #더 0에 가까운 값이 있나? +
        left += 1
    elif res > 0 : #더 0에 가까운 값이 있나? -
        right -= 1
    else: break #0이면 걍 바로

print(str(liq[rl])+' '+str(liq[rr]))

