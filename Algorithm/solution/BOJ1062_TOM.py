import sys

input = sys.stdin.readline

N, K = 0, 0
isLearn = [False] * 26
words = []
MAX_LEARN = 0


# 알파벳을 가르친다.
# a~z까지 가르쳐본다.
def learn_alpha(alpha, learn_cnt):
    global N, K, isLearn, words, MAX_LEARN
    # 현재 배운 단어개수가 K-5개인가?
    if learn_cnt == K - 5:
        # 현재 K-5개의 단어로 조합해서 최댓값을 찾는다.
        tmp = 0
        for word in words:
            flag = True
            for w in word:
                # 아직 남극언어 단어에 가르치지 않은 단어가 존재한다면
                if not isLearn[ord(w) - ord('a')]:
                    flag = False
                    break
            # K-5개의 단어가 모두 존재한다면
            if flag:
                tmp += 1
        MAX_LEARN = max(tmp, MAX_LEARN)
        return

        # 아직 K-5개가아니면
    for i in range(alpha, 26):
        # 아직 배우지 않은 상태면
        if not isLearn[i]:
            isLearn[i] = True  # 배운다.
            learn_alpha(i, learn_cnt + 1)
            isLearn[i] = False  # 다음단어를 배우기위해서 False를 한다.


def solution():
    global N, K, isLearn, words
    N, K = map(int, input().strip().split())
    # 선생님이 가르치는 글자수는 최소 5개(a,n,t,c,i)이다.
    if K < 5:
        return 0

    # 선생님이 가르치는 글자수가 26자라면
    # 학생들음 모든 단어를 읽을 수 있다.
    elif K == 26:
        return N

    for _ in range(N):
        word = input().strip()
        words.append(word.replace("antci", ""))

    # 먼저 a,c,i,n,t 5개는 가르쳤다고 치자.
    isLearn[ord('a') - ord('a')] = True
    isLearn[ord('c') - ord('a')] = True
    isLearn[ord('i') - ord('a')] = True
    isLearn[ord('n') - ord('a')] = True
    isLearn[ord('t') - ord('a')] = True

    # 나머지 알파벳 K-5개를 배운다.
    learn_alpha(alpha=0, learn_cnt=0)
    return MAX_LEARN


print(solution())