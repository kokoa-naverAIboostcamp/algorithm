# 19637번: IF문 좀 대신 써줘
# 방법 1
import sys
def boundary(a,x):
    lo,hi=0,len(a)
    while lo < hi:
        mid=(lo+hi)//2
        if x <= a[mid][0] : hi=mid
        else: lo = mid +1
    return lo

N,M=map(int,sys.stdin.readline().split())
style={}
for _ in range(N):
    name,value=sys.stdin.readline().strip().split()
    value=int(value)
    if value not in style:
        style[int(value)]=name
# sort
sort_style=sorted(style.items())
# search
for _ in range(M):
    power=int(sys.stdin.readline())
    print(sort_style[boundary(sort_style,power)][1])

# 방법 2
import sys
from bisect import bisect_left as bl
N,M=map(int,sys.stdin.readline().split())
styleN,styleV=[],[]
for _ in range(N):
    name,value=sys.stdin.readline().strip().split()
    styleN.append(name)
    styleV.append(int(value))

# search
for _ in range(M):
    power=int(sys.stdin.readline())
    print(styleN[bl(styleV,power)])