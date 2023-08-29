from itertools import combinations
import sys
input = sys.stdin.readline
INF = sys.maxsize

## 발상
## 치킨집들의 조합을 모두 구한다.
## B조합 치킨집들이 C집을 갈 때의 가장 작은 비용을 누적한다.
## B조합 치킨집들이 D집을 갈 때의 가장 작은 비용을 누적한다.
## ...
## 누적 중 이전 A조합 치킨집들이 모든 집을 방문했을 때의 최소비용보다 초과하게 될 경우
## B조합 치킨집의 탐색은 끝낸다.
## C조합 치킨집들을 탐색한다.
## 이렇게 모든 치킨집 조합을 탐색한다.
## 최종적으로 누적된 값을 출력한다.

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []
for x in range(n):
    for y in range(n):
        if lst[x][y] == 1:
            home.append((x, y))
        elif lst[x][y] == 2:
            chicken.append((x, y))

len_chicken = len(chicken)
len_home = len(home)

combi_chicken = list(combinations([i for i in range(len_chicken)], m))

sum = INF
for chicken_idxs in combi_chicken:
    temp = 0
    for home_idx in range(len_home):
        home_x, home_y = home[home_idx]

        min_cost = INF
        for chicken_idx in chicken_idxs:
            chicken_x, chicken_y = chicken[chicken_idx]
            cost = abs(chicken_x - home_x) + abs(chicken_y - home_y)
            min_cost = min(min_cost, cost)
        
        temp += min_cost
        if temp > sum:
            break
    else:
        sum = temp

print(sum)