from collections import defaultdict
import sys
input = sys.stdin.readline

def uu():
    word = input().rstrip()
    k = int(input())

    ## 각 문자의 인덱스를 모두 담은 딕셔너리
    dic = defaultdict(list)
    for i in range(len(word)):
        dic[word[i]].append(i)

    ## 결과값 초기화
    first_ans = float("inf")
    second_ans = 0
    
    ## 모든 문자에 대해
    alphabet = dic.keys()
    for alpha in alphabet:
        ## 해당 문자의 개수가 n보다 작으면 continue
        len_alpha = len(dic[alpha])
        if len_alpha < k:
            continue

        ## k를 반영한 간격으로 문자의 인덱스 차이를 통해 문자열 길이를 갱신
        for left in range(len_alpha - k + 1):
            right = left + k - 1
            ## 문자열 길이
            this_len = dic[alpha][right] - dic[alpha][left] + 1
            ## 첫번째 결과는 최소값으로 갱신
            first_ans = min(first_ans, this_len)
            ## 두번째 결과는 최대값으로 갱신
            second_ans = max(second_ans, this_len)

    ## 불가능하면 -1 출력
    if first_ans > 10000:
        return print(-1)
    
    ## 결과 출력
    print(first_ans)
    print(second_ans)
    

t = int(input())
for _ in range(t):
    uu()
