import sys
sys.stdin = open('input.txt')
# 조합 함수를 응용
def func(temp, idx):                    # 임시 누적함 temp, 리스트의 인덱스 idx
    global min

    start = 0                           # 시작 인덱스
    if temp:                            # temp가 0이 아니면
        start = idx + 1                     # start는 idx+1
    for i in range(start, n):           # start부터 마지막까지 순회
        if temp + sum(lst[i:n]) < b:        # 만약 (현재 temp값 + 나머지 모든 값)을 더했을 때
                                            # b보다 작으면 함수 끝(리스트가 내림차순이기 때문에)
            return

        temp += lst[i]                      # temp에 값 추가

        if b <= temp < min:                 # temp가 b보다 크고 min 보다 작다면(조건 만족)
            min = temp                      # min 갱신
            temp -= lst[i]                  # 마지막 더해준 값 다시 빼주고
            continue                        # for문으로(다음 숫자로)

        if temp > min:                      # temp가 min보다 크다면
            temp -= lst[i]                  # 마지막 더해준 값 다시 빼주고
            continue                        # for문으로(다음 숫자로)

        if min == b:                    # min이 b와 같다면 종료
            return

        idx = i                 # idx는 i로 갱신
        func(temp, idx)         # 현재 temp와 idx를 들고 다시 함수로
        temp -= lst[i]          # 함수 종료되면 temp에서 마지막 숫자 차감(for문 돌기 전 숫자 빼기)



T = int(input())
for case in range(T):
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)                  # 리스트 역배열
    min = sum(lst)                          # 조건을 만족하는 최소값 min
    func(0, 0)                              # min값을 찾는 함수
    print(f'#{case+1} {min-b}')



