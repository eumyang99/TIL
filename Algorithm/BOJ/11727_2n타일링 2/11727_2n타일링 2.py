import sys
input = sys.stdin.readline

## 점화식 규칙을 찾아보니 dp[i] = dp[i-2]*2 + dp[i] 였다.

n = int(input())
dp = [1,3]
for i in range(2, n):
    dp.append(dp[i-2]*2 + dp[i-1])

print(dp[n-1]%10007)





## 수학적으로 풀어봤다.
## 정사각형이 0개, 1개, 2개 ... 일 때 정사각형을 만드는 경우의 수는 2**n개
## 세로 막대기가 들어가는 공간은 정사각형+1 개
## 세로 막대기는 x개라고 할 때, 중복조합으로 정사각형+1 H x 로 하면 된다.
## 정사각형 경우 * 세로막대 경우 % 10007(문제의 특수 출력 조건)을 출력한다
# def combi(x, y):
#     n = x + y - 1
#     r = y
#     if 2*r > n:
#         r = n - r
    
#     result = 1
#     for i in range(n, n-r, -1):
#         result *= i
    
#     for i in range(r, 1, -1):
#         result = result // i
#     return result

# n = int(input())

# res = 0
# for i in range(n//2 + 1):
#     res += 2**i * combi(i+1, n-2*i)

# print(res%10007)