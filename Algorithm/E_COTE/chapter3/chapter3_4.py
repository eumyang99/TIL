root , div = map(int, input().split())

cnt = 0
while 1:
    if root % div == 0:     # 나누어 떨어지면 나누고
        root //= div
        cnt += 1            # cnt +1
    else:                   # 나누어 떨어지지 않으면
        root -= 1           # -1 하고
        cnt += 1            # cnt +1

    if root == 1:           # root가 1이면 종료
        break

print(cnt)