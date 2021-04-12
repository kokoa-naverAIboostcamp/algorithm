# 1062번: 가르침 (라이언)
from itertools import combinations
N,K=map(int,input().split())
# 가장 먼저 K값에 따라서 분류
if K<5:
    print(0)
    exit(0)
elif K==26:
    print(N)
    exit(0)
# 5개의 단어는 무조건 익혀야 하므로 -5해준다.
K-=5

# 모든 단어는 "anta"와 "tica"가 포함되어 있다.
# a,n,t,i,c 5개의 단어가 포함된다.
baseset=set('antic')
convert={chr(ord('a')+i):1<<i for i in range(26)}
words=[]
check=set()
ans=0
for _ in range(N):
    # 시작단어, 끝단어 제거
    word=set(input())-baseset
    # 5개의 단어로 읽을 수 있으면 ans +1
    if len(word) == 0:
        ans+=1
    # 배울 수 있는 단어보다 word의 길이가 같거나 짧은것만 읽을 수 있다.
    elif len(word) <= K:
        tmp=0
        # bit로 변환하여 저장
        for s in word:
            tmp +=convert[s]
        words.append(tmp)
        # 배워야 하는 단어의 후보군을 저장
        check |=word

check_size=len(check)
# 후보군을 bit로 변환한다.
check=map(lambda x: convert[x] ,check)
def compare(w):
    # 후보군의 전체 집합
    teach=sum(w)
    result=0
    # 각 단어들과 비교하여 읽을 수 있는지 counting한다.
    for word in words:
        if teach & word == word:
            result+=1
    return result

plus=max(map(compare,combinations(check,min(K,check_size))))
ans+=plus
print(ans)