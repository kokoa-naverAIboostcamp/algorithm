### 무지 ###
## 풀이 1 -> 1중 for 문
import sys

t = int(sys.stdin.readline())
answer = ""
while t > 0:
    t -= 1
    n = int(sys.stdin.readline())
    phone_book = [sys.stdin.readline()[:-1] for _ in range(n)]
    phone_book.sort()

    ans = "YES\n"
    for s1, s2 in zip(phone_book[:-1], phone_book[1:]):
        if s2.startswith(s1):
            ans = "NO\n"
            break
    answer += ans
print(answer)

## 풀이 2 -> 트라이 자료구조 (https://www.crocus.co.kr/1053), 라이언 풀이

import sys

class Node:
    def __init__(self, key, end=False):
        self.key = key  # 해당 노드의 문자
        self.end = end  # 문자열의 끝나는 위치 정보
        self.children = {}  # 자식 노드들의 정보를 담은 dict -> 연결된 문자(key)와 해당 문자의 노드(value)

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        # 입력 문자열의 각각의 문자들을 차례로 기존 노드에 연결되어 있는지 확인하며 순회
        for ch in string:
            if ch not in curr_node.children:  # 만약 존재하지 않으면 새롭게 생성
                curr_node.children[ch] = Node(ch)
            curr_node = curr_node.children[ch]
            if curr_node.end:
                return True

        # 모든 문자열 순회 후 curr_node는 마지막 문자 -> 문자열의 끝 정보를 넣어준다.
        curr_node.end = True
        return False


t = int(sys.stdin.readline())
answer = ""
for _ in range(t):
    n = int(sys.stdin.readline())
    trie = Trie()
    phone_book = [sys.stdin.readline()[:-1] for _ in range(n)]
    phone_book.sort()

    for num in phone_book:
        if trie.insert(num):
            answer += "NO\n"
            break
    else:
        answer += "YES\n"
print(answer)