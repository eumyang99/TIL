import sys
input = sys.stdin.readline

## 발상
## 현재 칸까지의 최대값을 누적해 감
## 현재 칸은 (두 칸 전 위아래 값 중 큰 값) 과 (한 칸 전 대각선에 있는 값) 중 큰 값에 누적한다.

def uu():
    n = int(input())
    lst = [[0] + list(map(int, input().split())) for _ in range(2)]
    
    for i in range(2, n+1):
        ## 두 칸 전의 위아래 값 중 큰 값
        two_step = max(lst[0][i-2], lst[1][i-2])
        lst[0][i] += max(two_step, lst[1][i-1])
        lst[1][i] += max(two_step, lst[0][i-1])

    print(max(lst[0][-1], lst[1][-1]))

t = int(input())
for _ in range(t):
    uu()
