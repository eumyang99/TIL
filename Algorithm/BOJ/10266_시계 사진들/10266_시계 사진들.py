import sys
input = sys.stdin.readline

## 정석 풀이
## 바늘이 위치할 수 있는 360,000개의 자리를 만들고 해당 위치에 바늘이 존재하면 1, 존재하지 않으면 0을 입력한다.
## a시계를 한번 더 연장하고 연장된 a시계에 b시계가 들어 있는지 확인한다.

n = int(input())

a_clock = list(map(int, input().split()))
b_clock = list(map(int, input().split()))
 
a_is = ["0"]*360000
b_is = ["0"]*360000

for i in range(n):
    a_is[a_clock[i]] = "1"
    b_is[b_clock[i]] = "1"

a_str = "".join(a_is)
b_str = "".join(b_is)

if b_str in a_str+a_str:
    print("possible")
else:
    print("impossible")







## 발상
## a시계와 b시계의 바늘 위치를 오름차순으로 정렬한다.
## a_dist와 b_dist 리스트 각각에 a시계의 바늘 간격들과 b시계의 바늘 간격들을 추가한다.
## a_dist 안에 b_dist가 들어 있는지 확인해야 하기 때문에 a_dist 한번 더 연장한다.
    ## 그러나 정렬된 a시계의 첫바늘과 마지막 바늘의 간격은 조정하는 계산이 필요하다. a_clock[0] - a_clock[-1] + 360000
    ## 따라서 a_dist + [a_clock[0] - a_clock[-1] + 360000] + a_dist 로 새로운 간격 리스트를 만든다.
## 이후 b_dist 안에 a_dist가 있는지 확인한다.

# n = int(input())

# a_clock = list(map(int, input().split()))
# b_clock = list(map(int, input().split()))
# for i in range(n):
#     if a_clock[i] == 0:
#         a_clock[i] = 360000
#     if b_clock[i] == 0:
#         b_clock[i] = 360000
# a_clock.sort()
# b_clock.sort()

# a_dist, b_dist = [], []
# for i in range(1, n):
#     a_dist.append(a_clock[i]-a_clock[i-1])
#     b_dist.append(b_clock[i]-b_clock[i-1])

# a_dist = a_dist + [a_clock[0] - a_clock[-1] + 360000] + a_dist
# ## 실패 함수
# pattern = [0]*(n-1)
# j = 0
# for i in range(1, n-1):
#     while j > 0 and b_dist[i] != b_dist[j]:
#         j = pattern[j-1]
#     if b_dist[i] == b_dist[j]:
#         j += 1
#         pattern[i] = j

# ## 비교
# j = 0
# for i in range(2*(n-1)):
#     while j > 0 and a_dist[i] != b_dist[j]:
#         j = pattern[j-1]
#     if a_dist[i] == b_dist[j]:
#         j += 1
#         if j == n-1:
#             print("possible")
#             break
# else:
#     print("impossible")