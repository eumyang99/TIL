import sys
sys.stdin = open('input.txt')

def permu(idx, r, temp, used):          # idx = temp에 더해진 횟수
                                        # r = 최대 더할 횟수
                                        # temp = 경우의 수에 따른 누적값
                                        # used = 사용된 인덱스
    global res
    if idx == r:                        # 충분히 더해졌으면
        if temp < res:                  # temp가 res 보다 작을 때
            res = temp                  # res 갱신 후 종료
            return

    else:                               # 더해질 것이 남아있으면
        for i in range(n):              # 0부터 n까지 순회하면서
            if i not in used:           # i가 기사용된 숫자가 아니라면
                objt = lst[idx][i]      # i 인덱스에 해당하는 더해질 숫자를 objt에 할당
                if temp + objt > res:       # temp에 objt를 더한 것이 res보다 벌써 크다면
                    continue                # 다음 숫자로
                temp += objt            # 그렇지 않다면 temp에 objt를 누적
                used.add(i)             # used에 i 추가
                permu(idx+1, r, temp, used)     # 이후 idx +1 높여서 temp와 used 들고 함수로
                used.remove(i)          # 위 함수를 빠져나왔으면
                temp -= objt            # used에서 i 제거, temp에서 objt 차감

    
T = int(input())
for case in range(T):
    n = int(input())        # 제품 수
    lst = [list(map(int, input().split())) for _ in range(n)]


    res = 99*n+1
    used = set()                # 사용된 인덱스를 저장할 세트
    permu(0, n, 0, used)
    print(f'#{case+1} {res}')


