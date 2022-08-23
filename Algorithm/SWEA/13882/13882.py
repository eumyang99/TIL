from pprint import pprint
import sys
sys.stdin = open('input.txt')



T = int(input())
for case in range(T):
    size = int(input())
    lst = [list(map(int, input().split())) for i in range(size)]


    def P(idx, n, r, res):
        global min_sum
        global temp
        if idx==r:
            min_sum = temp
            return
        for i in range(n):
            if i not in res: # res에 i가 없다면
                res.append(i) # res에 i 추가
                temp += lst[res.index(i)][i] # temp에 i의 인덱스(lst의 행)와 i(lst의 행 속 idx)에 해당하는 값을 temp에 추가

                if temp > min_sum: # 만약 쌓인 temp가 min_sum보다 크다면
                    temp -= lst[res.index(i)][i] # 마지막으로 추가된 값을 temp에서 빼고
                    res.pop() # res의 마지막 요소를 삭제, 이 친구 이후에 나오는 모든 경우의 수는 이미 min_sum값을 초과했으니 
                    continue # 다시 for문 처음으로 돌아감

                P(idx + 1,n, r, res) # 위 if문에 걸리지 않고 다음 숫자를 res에 추가하기 위해 다시 함수에 진입
                temp -= lst[res.index(i)][i] # 함수가 다 끝나고 min_sum 값이 갱신되었으면 다시 다른 경우의 수로 돌아가기 위해 temp에서 차례차례 차감
                res.pop() # res에 쌓인 것도 차례차레 삭제



    min_sum = 0
    for i in range(len(lst)):
        min_sum += lst[i][i] # lst의 우하향 대각선을 합한 것을 임시 min_sum으로 상정
    temp = 0
    P(0, size, size, [])

    print(f'#{case+1} {min_sum}')


