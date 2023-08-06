import sys
input = sys.stdin.readline

## 진짜 어려웠던 DP 문제
## 풀이는 이것을 참고했음
## https://www.youtube.com/watch?v=5MXOUix_Ud4 


n = int(input())
lst = []
a, b = map(int, input().split())
lst.append(a)
lst.append(b)
for _ in range(n-1):
    a, b = map(int, input().split())
    lst.append(b)


dp = [[float("inf")]*(n) for _ in range(n)]

for x in range(n):
    a = 0
    for y in range(n-x):
        b = a + x
        if a == b:
            dp[a][b] = 0
            a += 1
            continue
        mini = dp[a][b]
        for i in range(x):
            temp = dp[a][a+i] + dp[a+i+1][b] + lst[a-1]*lst[a+i]*lst[b]
            if temp < mini:
                mini = temp
        dp[a][b] = mini 
        a += 1

print(dp[0][-1])














## 틀린 방법
## 행렬 곱셈 횟수 중 가장 작은 것들을 찾아서 먼저 계산
## 그러나 예외 케이스를 발견 (ex 1 2 / 2 10 / 10 3 / 3 1)
## 모범적인 풀이인 DP를 사용해서 풀기로 함

# def left_search(idx):
#     l_idx = idx - 1
#     while l_idx in used and l_idx != 0:
#         l_idx -= 1
#     return l_idx

# def right_search(idx):
#     r_idx = idx + 1
#     while r_idx in used and r_idx != n:
#         r_idx += 1
#     return r_idx


# n = int(input())

# lst = []
# calc = [float("inf")]

# for i in range(n):
#     if i == 0:
#         x, y = map(int, input().split())
#         lst.append(x)
#         lst.append(y)
#     else:
#         x, y = map(int, input().split())
#         lst.append(y)

# for i in range(n-1):
#     calc.append(lst[i] * lst[i+1] * lst[i+2])
# else:
#     calc.append(float("inf"))
    
# res = 0
# used = set()
# for _ in range(n-1):
#     min_num = min(calc)
#     min_idx = calc.index(min_num)
#     for i in range(n+1):
#         if calc[i] == min_num and i not in used:
#             if lst[i] > lst[min_idx]:
#                 min_idx = i
#     res += min_num
#     used.add(min_idx)
#     calc[min_idx] = float("inf")

#     changing_left_idx = left_search(min_idx)
#     changing_right_idx = right_search(min_idx)

#     if changing_left_idx != 0:
#         left_num_idx = left_search(changing_left_idx)
#         calc[changing_left_idx] = lst[left_num_idx] * lst[changing_left_idx] * lst[changing_right_idx]

#     if changing_right_idx != n:
#         right_num_idx = right_search(changing_right_idx)
#         calc[changing_right_idx] = lst[right_num_idx] * lst[changing_right_idx] * lst[changing_left_idx]

# print(res)

