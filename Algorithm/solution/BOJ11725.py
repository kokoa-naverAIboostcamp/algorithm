### 라이언 ###
#방법 1
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
def find_parent(n):
    for i in node[n]:
        if result[i] == 0:
            result[i]=n
            find_parent(i)


N=int(input())
node=defaultdict(list)
result=[0]*(N+1)
result[1]=1
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
find_parent(1)
print(*result[2:],sep='\n',end='')

#방법 2
import sys
from collections import defaultdict
from collections import deque

N=int(input())
node=defaultdict(list)
result=[0]*(N+1)
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

q=deque()
q.appendleft(1)
result[1]=1

while q:
    parent=q.pop()
    for n in node[parent]:
        if result[n]==0:
            result[n]=parent
            q.appendleft(n)
print(*result[2:],sep='\n',end='')