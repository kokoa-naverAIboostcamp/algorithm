# 9322번: 철벽 보안 알고리즘
T=int(input())
for _ in range(T):
    N=int(input())
    first_key={key:idx for idx,key in enumerate(input().split())}
    second_key={idx:first_key[key] for idx,key in enumerate(input().split())}
    # 초기화
    text=[0]*N
    encryption=input().split()
    for idx,key in enumerate(encryption):
        text[second_key[idx]] = key
    print(*text,sep=' ')