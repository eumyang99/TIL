import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

# T = int(input())
# for case in range(T):
a, b =[], []
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_score = 0
b_score = 0
for i in range(10):
    if a[i] > b[i]:         # a가 이겼을 때
        a_score += 3
    elif a[i] < b[i]:       # b가 이겼을 때
        b_score += 3
    else:                   # 비겼을 때
        a_score += 1
        b_score += 1

if a_score > b_score:           # a 점수가 높으면 출력
    print(a_score, b_score)
    print('A')
elif a_score < b_score:         # b 점수가 높으면 출력
    print(a_score, b_score)
    print('B')
else:                           # 점수가 같으면
    print(a_score, b_score)
    for i in range(9, -1, -1):  # a리스트 b리스트 거꾸로 탐색하면서
        if a[i] > b[i]:         # 보다 큰 녀석이 나타나면
            print('A')          # 그녀석 출력하고 break
            break
        elif a[i] < b[i]:
            print('B')
            break
    else:                       # 모든 점수가 같으면 출력
        print('D')
