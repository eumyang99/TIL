import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, m, k = map(int, input().split())
    son = list(map(int, input().split()))

    son.sort()                              # 손님 오름차순 정렬

    d = son[0] // m                        # 첫 손님 / m의 몫
    brd = (son[0] // m) * k                 # 첫 손님 맞이할 때 가진 빵 개수
    for i in range(n):                      
        if d != son[i] // m:                # 만약 i번째 손님에 대한 몫이 기존의 몫과 달라졌다면
            brd += ((son[i] // m)-d)*k          # 빵 추가
            d = son[i] // m                 # 몫을 갱신하고
        
        brd -= 1                            # 손님 만날 때마다 빵 -1
    
        if brd < 0:                         # 빵이 부족하다면 실패
            print(f'#{case+1} Impossible')
            break
    else:
        print(f'#{case+1} Possible')        # 손님 전체 순회했다면 성공


