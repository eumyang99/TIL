import sys
sys.stdin = open('input.txt')

def func():
    if not exp:                                     # 만약 exp가 비어 있다면 만날 수 있는 점이 없다는 것
        return print(f'#{case+1} 0')                # 0 출력

    exp.sort(reverse=True)                          # 사용한 점을 pop해서 없앨 예정이기 때문에
                                                    # 두 점 사이의 거리가 짧은 녀석들이 맨뒤로 가게 역으로 정렬
    
    used = set()                                    # 만나서 파괴된 원자들을 기록할 세트
    res = 0                                         # 출력될 결과
    dist, p, q = exp.pop()                          # exp에서 먼저 pop을 하고
    res += lst[p][-1] + lst[q][-1]                  # 사용된 두 원자의 에너지를 누적
    used.add(p)                                     # 두 원자 사용 처리
    used.add(q)
    while exp:                                      # 사용할 원자가 없을 때까지
        d, x, y = exp.pop()                         # d, x, y에 다음 녀석을 pop해서 저장
        if dist == d and p == x and y not in used:  # 먼저 pop된 녀석과 지금 pop한 녀석이 동시에 사라질 녀석들이라면
            used.add(y)                                 # 방금 사용된 원자 사용 처리하고
            res += lst[y][-1]                           # 에너지 누적
        if x not in used and y not in used:         # 두 점 모두 사용된적 없는 원자라면
            used.add(x)                                 # 두 점 사용처리하고
            used.add(y)
            res += lst[x][-1] + lst[y][-1]              # 에너지 누적
            dist, p, q = d, x, y                        # 이 녀석들과 동시에 파괴될 녀석들이 있을 수 있으니
                                                        # dist, p, q 갱신

        
    print(f'#{case+1} {res}')
# 상(0), 하(1), 좌(2), 우(3)


T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key=lambda x: x[0])                                    # 평면에서 가장 왼쪽부터 있는 원자순으로 정렬
    
    exp = []                                                        # 만날 가능성이 있는 원자들을 모아 놓을 리스트

    for p in range(n-1):                                            # 모든 원자를 두개씩 비교하며
        for q in range(p+1, n):         
            dx = lst[p][0] - lst[q][0]                              # 두 원자의 x값, y값 차이를 저장
            dy = lst[p][1] - lst[q][1]
            
            # 왼쪽의 점부터 탐색하기 때문에 조건을 만들기가 보다 수월했음

            if dx == 0:                                             # 두 점이 세로로 겹치면서 만날 가능성이 있으면
                if lst[p][2] == 0 and lst[q][2] == 1 and dy < 0:    
                    dist = abs(dy)      
                    exp.append([dist, p, q])                        # 두 점 사이의 거리와 두 점의 원본 리스트 상 인덱스를 저장 
                elif lst[p][2] == 1 and lst[q][2] == 0 and dy > 0:
                    dist = abs(dy)
                    exp.append([dist, p, q])

            elif dx == dy:                                          # 두 점의 기울기가 1이면서 만날 가능성이 있으면
                if lst[p][2] == 0 and lst[q][2] == 2 and dy < 0:
                    dist = abs(dx) + abs(dy)
                    exp.append([dist, p, q])                        # 두 점 사이의 거리와 두 점의 원본 리스트 상 인덱스를 저장
                elif lst[p][2] == 3 and lst[q][2] == 1 and dy < 0:
                    dist = abs(dx) + abs(dy)
                    exp.append([dist, p, q])


            elif dx*-1 == dy:                                       # 두 점의 기울기가 -1이면서 만날 가능성이 있으면
                if lst[p][2] == 3 and lst[q][2] == 0 and dy > 0:
                    dist = abs(dx) + abs(dy)
                    exp.append([dist, p, q])                        # 두 점 사이의 거리와 두 점의 원본 리스트 상 인덱스를 저장
                elif lst[p][2] == 1 and lst[q][2] == 2 and dy > 0:
                    dist = abs(dx) + abs(dy)
                    exp.append([dist, p, q])

            elif dy == 0:                                           # 두 점이 가로로 겹치면서 만날 가능성이 있으면
                if lst[p][2] == 3 and lst[q][2] == 2:
                    dist = abs(dx)
                    exp.append([dist, p, q])                        # 두 점 사이의 거리와 두 점의 원본 리스트 상 인덱스를 저장

    # 종료 처리를 위해 함수 사용
    func()
                