# 6503번: 망가진 키보드
while True:
    m=int(input())
    # 종료 조건
    if m == 0 : break
    input_str=input()
    ans,start,end=0,0,0
    str_dict=dict()
    for c in input_str:
        if c not in str_dict:
            if len(str_dict) == m:
                ans=max(ans,end-start)
                while start < end:
                    str_dict[input_str[start]]-=1
                    if str_dict[input_str[start]] == 0:
                        del str_dict[input_str[start]]
                        start +=1
                        break
                    start+=1
            str_dict[c]=1
        else:
            str_dict[c]+=1
        end+=1
    ans = max(ans, end - start)
    print(ans)