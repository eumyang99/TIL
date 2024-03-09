## 발상
## dfs로 각 그룹의 사이즈와 사탕의 총 개수를 기록
## dp(배낭)로 최대값 찾음

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
edges_dic = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    edges_dic[s].append(e)
    edges_dic[e].append(s)

visited = [False] * (n+1)
candy_by_group_size = []
for child in range(1, n+1):
    if visited[child]: continue
    visited[child] = True
    group_size = 1
    total_candy = candy[child]
    stack = [child]
    while stack:
        start_child = stack.pop()
        for next_child in edges_dic[start_child]:
            if visited[next_child]: continue
            visited[next_child] = True
            group_size += 1
            total_candy += candy[next_child]
            stack.append(next_child)
    else:
        if k <= group_size: continue 
        candy_by_group_size.append((group_size, total_candy))

dp = [0] * k
for group_size, candy in candy_by_group_size:
    for i in range(k-1, group_size-1, -1):
        if dp[i] < candy + dp[i - group_size]:
            dp[i] = candy + dp[i - group_size]


print(dp[-1])
