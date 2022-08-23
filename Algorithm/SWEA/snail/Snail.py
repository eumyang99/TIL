import sys
sys.stdin = open('input.txt')



t = int(input())
for case in range(t):
    n = int(input())
    # 정답이 들어갈 빈 리스트 생성
    res = [[0]*n for _ in range(n)]

    # 현재 위치 H
    H = [0,0]
    # 달팽이가 움직이면서 기록할 숫자
    cnt = 1

    # 행과 열에서 한번에 쭉 움직일 거리 리스트
    # 예를 들어 n = 4이면 3, 1 /// n = 5이면 4,2,1 /// n= 6이면 5,3,1
    # while로 풀까 for로 풀까 고민하다가 for로 결정하고 만든 리스트
    rept_lst = []
    for i in range((n-1)//2):
        rept_lst.append((n-1)-2*i)
    rept_lst.append(1)

    for i in rept_lst:
        # 현재 위치에 숫자를 기록 후
        # i번 오른쪽으로 이동하면서 숫자기록, 카운트+1
        for _ in range(i):
            res[H[0]][H[1]] = cnt
            H[1] += 1
            cnt += 1
            # 만약 카운트가 최대 이동 횟수(n=4이면 16)에 도달하면 그만
            if cnt == n*n+1:
                break
        # 마찬가지로 카운트가 최대 이동 횟수(n=4이면 16)에 도달하면 그만
        if cnt == n*n+1:
            break
        
        # 현재 위치에 숫자를 기록 후
        # i번 아래쪽으로 이동하면서 숫자기록, 카운트+1
        for _ in range(i):
            res[H[0]][H[1]] = cnt
            H[0] += 1
            cnt += 1

        # 현재 위치에 숫자를 기록 후
        # i번 왼쪽으로 이동하면서 숫자기록, 카운트+1
        for _ in range(i):
            res[H[0]][H[1]] = cnt
            H[1] -= 1
            cnt += 1

        # 위로 움직일 차례에서는
        for x in range(i):
            # i-1번째 움직임에서는 위로 올라가지 않고 오른쪽으로 이동
            if x == i-1:
                res[H[0]][H[1]] = cnt
                cnt += 1
                H[1] += 1
                break
            # 그렇지 않다면
            # 현재 위치에 숫자를 기록 후
            # i번 위쪽으로 이동하면서 숫자기록, 카운트+1     
            else:
                res[H[0]][H[1]] = cnt
                cnt += 1
                H[0] -= 1
        # 바깥 정사각형에 다 기록했으니
        # 안쪽 정사각형에 기록하러 반복 고고

    print(f'#{case+1}')
    for i in range(n):
        s = " ".join(map(str, (res[i])))
        print(s)
    









