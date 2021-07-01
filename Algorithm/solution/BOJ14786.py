# Ax+Bsinx=C
### 찰스 ###

# reference : https://ratel35.tistory.com/350
from math import sin


A, B, C = map(int, input().split())

def fn(x):
    return A*x + B*sin(x) - C

# Ax 는 C -|B| ~ c +|B| 사이에 있다. 즉 (C -|B|)/A  <= x <=  (c +|B|)/A (A가 양수일 경우)

l, r = (C-B)/A, (C+B)/A  #  0 < B < A

while True:
    m = (l+r)/2
    if -(1e-9) < (r-l) < 1e-9 : break
    if fn(l)*fn(m) < 0: r = m
    elif fn(m)*fn(r) < 0: l = m
    
print(m)

