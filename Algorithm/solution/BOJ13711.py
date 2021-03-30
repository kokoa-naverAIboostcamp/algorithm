### 라이언 ###
from bisect import bisect_left as bl
import sys

def lcs4():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    tmp = [0 for _ in range(N+1)]

    for i in range(N):
        tmp[B[i]] = i
    A=[tmp[A[i]] for i in range(N)]

    lis=[-float('inf')]
    for num in A:
        if lis[-1] < num:
            lis.append(num)
        else:
            lis[bl(lis,num)]=num

    print(len(lis)-1)
lcs4()



### ??? ###