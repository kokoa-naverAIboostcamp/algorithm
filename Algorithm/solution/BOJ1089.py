### 라이언 ###
import sys

def get_input():
    info_board = []
    n = int(sys.stdin.readline())
    # 5줄로 입력을 받음
    for _ in range(5):
        info_board.append(sys.stdin.readline())
    return (n, info_board)

def main(N, info_board):
    sample='''\
###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###'''
    sample_list=sample.split('\n')
    number=[]

    # 한 숫자씩 읽기
    for std in range(0,4*10-1,4):
        tmp=list(map(lambda x: x[std:std + 3], sample_list))
        point=set()
        for i in range(5):
            for j in range(3):
                if tmp[i][j] == '#':
                    point.add((i,j))
        number.append(point)


    def num_matching(board):
        ans=[]
        compare=set()
        for i in range(5):
            for j in range(3):
                if board[i][j] == '#':
                    compare.add((i,j))

        for n,n_set in enumerate(number):
            # 불을 켜서 가능한 번호
            if compare - n_set== set():
                ans.append(n)

        if not ans:
            print(-1)

        return ans

    result=0
    cases=[]

    # N개의 숫자에 대해서 처리
    for std in range(0,4*N-1,4):
        cases.append(num_matching(list(map(lambda x: x[std:std+3],info_board))))

    case_cnt=[len(l) for l in cases]
    sum_cnt=1
    for num in case_cnt:
        sum_cnt*=num

    for i,C in enumerate(cases):
        cnt=1
        for num in [n for j,n in enumerate(case_cnt) if j!=i]:
            cnt*=num

        for num in C:
            result+=num*cnt*10**(N-i-1)

    print(result/sum_cnt if sum_cnt !=0 else -1)
    return result/sum_cnt if sum_cnt !=0 else -1

if __name__ == "__main__":
    a, b = get_input()
    main(a, b)

### ??? ###