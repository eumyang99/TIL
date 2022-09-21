import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)                    # 화물 내림 차순 정렬
    t.sort()                                # 트럭 오름 차순 정렬

    res = 0
    able_truck = m                          # 가용한 트럭 수
    for stuff in w:                             # 화물을 무거운 녀석부터 순회하면서
        for i in range(able_truck-1, -1, -1):                  # 용량이 큰 트럭부터
            if t[i] >= stuff:                   # 적재가 가능하면 
                res += stuff                    # res에 무게 더하고
                t.pop()                         # 적재한 트럭 출발
                able_truck -= 1                 # 가용한 트럭 수 -1
                break                           # 다음 화물 적재하러 고고
    
    print(f'#{case+1} {res}')
