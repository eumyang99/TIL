import sys
input = sys.stdin.readline

def factorial(s, e):                    # s부터 e까지 곱했을 때의 값(s > e)
    if s == e:
        return e
    res = s * factorial(s-1, e)
    return res


T = int(input())
for case in range(T):
    L, R = map(int, input().split())

    if L == R:                          # 서쪽과 동쪽의 사이트가 같은 경우에는 경우의 수가 1개
        print(1)
    else:                               # 그렇지 않을 경우
        temp = R - L                    # L combination R의 값을 구해서 출력
        if temp < L:
            print(factorial(R, R-temp+1)//factorial(temp, 1))
        else:
            print(factorial(R, R-L+1)//factorial(L, 1))

