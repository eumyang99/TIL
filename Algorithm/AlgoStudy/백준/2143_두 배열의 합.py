## 두 배열의 부배열의 합을 key값으로 개수를 map에 기록
## 두 맵의 key값을 비교해서 결과에 추가

from collections import defaultdict
import sys

input = sys.stdin.readline

t = int(input())
n, arr1 = int(input()), list(map(int, input().split()))
m, arr2 = int(input()), list(map(int, input().split()))

answer = 0
size = [n, m]
accu = [[0] + arr1,  [0] + arr2]
memo = [defaultdict(int), defaultdict(int)]

for each in [0, 1]:
    for i in range(1, size[each]+1):
        accu[each][i] += accu[each][i-1]

for each in [0, 1]:
    for s in range(1, size[each]+1):
        for e in range(s, size[each]+1):
            val = accu[each][e] - accu[each][e-s]
            memo[each][val] += 1

for num, cnt in memo[0].items():
    if not memo[1][t-num]: continue
    answer += cnt * memo[1][t-num]

print(answer)