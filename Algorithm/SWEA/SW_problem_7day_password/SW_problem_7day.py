import sys
sys.stdin = open('input.txt')

T = 10
for cs in range(T):
    case = int(input())
    a = list(map(int, input().split()))

    reduce = min(a) // 15
    for i in range(len(a)):
        a[i] = a[i] - (15 * (reduce-1))

    while 1:
        for i in range(1, 6):
            a[0] = a[0] - i
            a.append(a.pop(0))
            if a[-1] <= 0:
                a[-1] = 0
                break
        if a[-1] == 0:
            break
    print(f'#{case}', end=" ")
    print(*a)