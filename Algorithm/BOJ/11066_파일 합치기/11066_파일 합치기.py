import sys
input = sys.stdin.readline
INF = sys.maxsize

## 발상 
## DP 공부하면서 배운 bottom-top을 활용했다.
## a ~ b까지의 비용을 arr[a][b]에 담는다.
## 저장될 비용은 a~b를 이루는 구간의 경우의 수
## 해당 구간의 각 비용 arr[a][mid] + arr[mid+1][b]
## 해당 구간의 각 크기 a~mid까지의 구간 크기 + mid+1~b까지의 구간 크키)
## 비용과 크기를 전부 비교해서 가장 작은 값을 arr[a][b]에 갱신하며 쌓아올린다.
## 그리고 arr[0][-1]을 출력하면 처음부터 끝까지 모든 파일을 합쳤을 때 최소 비용이 나온다.

## 크누스 알고리즘
## 이걸 활용하면 시간을 10배 정도 줄일 수 있다고 한다.
## 공부할 예정


def uu():
    n = int(input())
    lst = list(map(int, input().split()))

    accu = [0, lst[0]]
    for i in range(1, n):
        accu.append(lst[i] + accu[-1])

    arr = list([0]*n for _ in range(n))

    ## 대각선 개수
    for i in range(n-1): # 0 1 2 3
        ## 대각선 당 채울 칸 수
        for p in range(n-i-1): # 0123 012 01 0
            x = p
            y = x + i + 1
            
            left_x, left_y = x, x
            right_x, right_y = x+1, y
            mini = INF

            ## 이 부분을 크누스 알고리즘을 활용하면 순회하는 회수를 줄일 수 있다고 한다.
            for _ in range(y-x):
                left_cost = arr[left_x][left_y]
                right_cost = arr[right_x][right_y]
                cost = left_cost + right_cost + accu[y+1] - accu[x]

                if cost < mini:
                    mini = cost

                left_y += 1
                right_x += 1

            arr[x][y] = mini

    print(arr[0][-1])
