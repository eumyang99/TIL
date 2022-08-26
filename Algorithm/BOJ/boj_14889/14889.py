import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')


def combi(idx, n, r, res):          # 조합을 만드는 함수
    if idx == r:
        a.append(res[:])
        return

    start = 0
    if res:
        start = max(res) + 1

    for i in range(start, n):
        res.append(i)
        combi(idx+1, n, r, res)
        res.pop()

T = 3
for case in range(T):
    size = int(input())
    lst = [list(map(int, input().split())) for i in range(size)]

    a = []                                      # 가능한 조합을 담을 빈 리스트 a
    combi(0, size, size//2, [])                 # ex) size가 4인 경우 2개씩, 6인 경우 3개씩 조합
    print(a)

    res = 9999999                               # 최소값을 찾기 위해 임의의 큰 숫자 할당
    for i in range(len(a)//2):                  # 말로 설명하기 어려움ㅠㅠ
        p = a[i]                                # 그림으로 설명 가능
        q = a[len(a)-1-i]
        temp_a = 0
        temp_b = 0
        for x in range(size//2 - 1):
            for y in range(x+1, size//2):
                temp_a += lst[p[x]][p[y]] + lst[p[y]][p[x]]
                temp_b += lst[q[x]][q[y]] + lst[q[y]][q[x]]
        temp = abs(temp_a - temp_b)             # 비교한 값의 차이가 가장 작은 것을 temp에 저장
        if res > temp:                          # 조건에 맞으면 res에 temp 할당
            res = temp

    print(res)


