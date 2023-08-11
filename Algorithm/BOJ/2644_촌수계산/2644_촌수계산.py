from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

## 발상
## 다익스트라로 풀었다.
## 그런데 BFS, DFS로 풀 수 있는 문제이다.
## 완전탐색과 다익스트라 중 무엇이 더 효율적인지 판단하기 어렵다.
## 이에 대해 다시 생각해 볼 필요가 있다.

def dijk(start):
    weight = [INF] * (n+1)
    weight[start] = 0
    pq = [(0, start)]

    while pq:
        w, e = pq.pop()

        if e == target[1]:
            return weight[e]
        
        if w > weight[e]:
            continue
        for nw, ne in dic[e]:
            new_w = w + nw
            if weight[ne] > new_w:
                weight[ne] = new_w
                heapq.heappush(pq, (new_w, ne))
    else:
        return -1
        
            


n = int(input())
target = tuple(map(int, input().split()))
m = int(input())
dic = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    dic[s].append((1, e))
    dic[e].append((1, s))

print(dijk(target[0]))

