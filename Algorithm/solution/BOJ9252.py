### 라이언 ###
# 9252번: LCS 2
A,B=input(),input()
def lcs(A,B):
    dp=['']*len(B)
    for i in range(len(A)):
        max_dp=''
        for j in range(len(B)):
            if len(max_dp) < len(dp[j]):
                max_dp=dp[j]
            elif A[i] == B[j]:
                dp[j]=max_dp+B[j]

    # 가장 큰 값 찾기
    ans=''
    for s in dp:
        if len(ans) < len(s):
            ans=s
    print(len(ans))
    if len(ans):
        print(ans)

lcs(A,B)