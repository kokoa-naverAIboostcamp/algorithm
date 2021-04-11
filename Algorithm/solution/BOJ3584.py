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
    
    
####################################################################

### 무지 ###
import sys

T = int(sys.stdin.readline())                               # 테스트 케이스 개수
for _ in range(T):
    N = int(sys.stdin.readline())                           # 트리의 노드 개수
    nodes = [0] * (N + 1)
    for _ in range(N - 1):
        parent, child = map(int, sys.stdin.readline().split())
        nodes[child] = parent

    A, B = map(int, sys.stdin.readline().split())           # 가장 가까운 공통 조상을 구할 두 노드
    parent_of_A = [A]                                       # A와 B의 부모들의 list를 각각 구한다.
    parent_of_B = [B]
    
    while nodes[A] != 0:                                    # 루트 노드가 나올 때까지 거꾸로 올라가면서 list에 추가
        parent_of_A.append(nodes[A])
        A = nodes[A]
    while nodes[B] != 0:                                    # B에 대해서도 마찬가지로 
        parent_of_B.append(nodes[B])
        B = nodes[B]

    # 이제 A와 B의 가장 가까운 공통 조상을 구한다.
    ## 방법 1 -> O(N^2) 완전탐색 방법
    # for a in parent_of_A:
    #     if a in parent_of_B:
    #         print(a)
    #         break

    ## 방법 2 -> O(N^2) 완전탐색 방법 (1번과 달리 B의 부모 리스트는 역순으로 탐색)
    # for a in parent_of_A:
    #     flag = False
    #     for b in parent_of_B[::-1]:
    #         if a == b:
    #             flag = True
    #             break
    #     if flag:
    #         print(a)
    #         break

    ## 방법 3 -> 루트노드 부터 탐색 방법
    # 파이썬은 인덱스가 -1로 내려가도 out of range 발생하지 않음
    # 파이썬에서 -1은 마지막 원소 의미 -> 그래서 이런 에러가 찾기 힘들고
    # 이를 방지하기 위해 zip으로 묶으면 좋다!
    pre = 0
    for a, b in zip(parent_of_A[::-1], parent_of_B[::-1]):
        if a == b:
            pre = a
        else:
            print(pre)
            break
    else:
        print(pre)
