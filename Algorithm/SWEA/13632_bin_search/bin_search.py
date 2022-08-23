import sys
sys.stdin = open("input.txt")

T = int(input())
for case in range(T):
    size, a_goal, b_goal = map(int, (input().split()))

    a_L = 1
    a_R = size
    b_L = 1
    b_R = size
    cnt_a = 0
    cnt_b = 0


    while True:
        cnt_a += 1
        center_a = int((a_L+a_R)/2)
        if a_L > a_R: # 좌우가 역전되면 cnt_a에 큰 숫자를 넣어서 끝냄
            cnt_a = size
            break
        elif center_a == a_goal: # 목표를 찾으면 끝냄
            break
        elif center_a < a_goal: # 센터가 목표보다 작으면
            a_L = center_a # 왼쪽 인덱스를 센터로
        elif center_a > a_goal: # 센터가 목표보다 크면
            a_R = center_a # 오른쪽 인덱스를 센터로


    while True:
        cnt_b += 1
        center_b = int((b_L+b_R)/2)
        if b_L > b_R:
            cnt_b = size
            break
        elif center_b == b_goal:
            break
        elif center_b < b_goal:
            b_L = center_b
        elif center_b > b_goal:
            b_R = center_b

    if cnt_a < cnt_b:
        print(f'#{case+1} A')
    elif cnt_a > cnt_b:
        print(f'#{case+1} B')
    elif cnt_a == cnt_b:
        print(f'#{case+1} 0')



