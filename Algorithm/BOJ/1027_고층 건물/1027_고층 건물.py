import sys
input = sys.stdin.readline

## 발상 : 왼쪽에서 오른쪽을 바라봤을 때 보이면 오른쪽에 있는 빌딩도 왼쪽 빌딩이 보인다
## 왼쪽에서 오른쪽만 바라본다
## 왼쪽 빌딩에서 오른쪽 빌딩을 바라봤을 때 기존 최고 각도보다 높다면
## 왼쪽 빌딩에서 보이는 빌딩 수를 +1
## 바라봐진 오른쪽 빌딩에서 보이는 빌딩 수 +1
## 최고 각도를 갱신한다.
## 가장 많은 빌딩이 보이는 수를 출력한다.

INF = sys.maxsize

n = int(input())
lst = list(map(int, input().split()))
res = [0] * (n+1)

for x in range(n-1):
    angle = -INF
    for y in range(x+1, n):
        temp = (lst[y] - lst[x]) / (y-x)
        if temp > angle:
            res[x] += 1
            res[y] += 1
            angle = temp

print(max(res))