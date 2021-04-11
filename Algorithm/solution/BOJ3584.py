# 죠르디
import sys
r = sys.stdin.readline
    
T = int(r())                        # test case 수
ans = []
for _ in range(T):                  # test case 만큼 실행
    N = int(r())                    # node 개수
    edges = [0 for _ in range(N+1)] # 1부터 인덱싱하는 edges
    for i in range(N-1):            # edge의 개수는 n-1
        p, c = map(int, r().split())# 부모 자식 
        edges[c]=p                  # 자식노드의 값을 인덱스로 하고 그 인덱스의 값을 부모 노드로 정의
    a, b = map(int, r().split())    # 공통 조상이 있는 대상
    
    pars_a = [a]                    
    parent = edges[a]               # a의 부모
    while parent:                   # 부모가 있는 한 탐색
        pars_a.append(parent)       # 부모의 부모를 반복하여 추가
        parent = edges[parent]        
    
    pars_b = [b]                    
    parent = edges[b]               # b의 부모
    while parent:                   # 같은방법으로 탐색
        pars_b.append(parent)       # 부모의 부모를 반복하여 추가
        parent = edges[parent]
        
    level_a = len(pars_a)-1         # 최상위 부모는 공통이므로
    level_b = len(pars_b)-1         # 위에서 부터 탐색
    
    while pars_a[level_a] == pars_b[level_b]:
        level_a -= 1
        level_b -= 1
        
    ans.append(pars_a[level_a+1])    
    
for node in ans:
    print(node)