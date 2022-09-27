import sys
sys.stdin = open('input.txt')

def bin_search(lst, target):        # 탐색할 리스트와 찾을 숫자
    start = 0                       # 왼쪽 idx
    end = len(lst) - 1              # 오른쪽 idx

    LC , RC = 0, 0                  # 왼쪽 카운트, 오른쪽 카운트
    while start <= end:             # 왼쪽idx가 오른쪽 idx보다 작거나 같을 때까지 반복
        m = (start + end) // 2      # 중간지점
        if lst[m] == target:        # 중간지점이 target이면 1 return
            return 1
        elif lst[m] > target:       # 중간지점이 타겟보다 크면
            end = m - 1             # 왼쪽 부분으로 탐색 범위 한정
            LC += 1                 # 왼쪽 카운트 +1
            if LC == 2:             # 왼쪽 카운트가 2이면
                return 0            # 실패, 0 리턴
            RC = 0                  # 오른쪽 카운트 0 으로 초기화
        elif lst[m] < target:       # 오른쪽은 상동
            start = m + 1
            RC += 1
            LC = 0
            if RC == 2:
                return 0

    else:                           # 오른쪽 idx가 왼쪽 idx보다 작다면 없는 숫자
        return 0                    # 0 리턴



T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()                                  # 문제에서 정렬을 하라고 함
    targets = list(map(int, input().split()))   

    res = 0                                     # 출력할 결과
    for target in targets:                      
        res += bin_search(lst, target)          # 리스트와 타겟을 하나씩 함수에 넣고 return값을 res에 더함
    
    print(f'#{case+1} {res}')