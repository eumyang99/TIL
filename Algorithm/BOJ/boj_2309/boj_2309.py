import sys
input = sys.stdin.readline

# 리스트 sum 함수
def my_sum(lst):
    res = 0
    for i in lst:
        res += i
    return res

# lst에 int로 9개 숫자 받음
lst = [int(input()) for i in range(9)]

# 정답 저장할 빈 리스트 생성
res = []

# 9개 숫자 중 2개를 빼서 모두 더했을 때 합이 100이면 되니까
# 먼저 하나를 빼고
for x in range(9):
    test_1 = lst[:]
    test_1.pop(x)
    # 두개를 빼서
    for y in range(8):
        test_2 = test_1[:]
        test_2.pop(y)
        # 남은 숫자의 합이 100이면
        if my_sum(test_2) == 100:
            # res에 저장하고 전체 for문 종료
            res = test_2
            break
    if res:
        break

# res 버블 정렬
for i in range(6, 0, -1):
    for x in range(i):
        if res[x] > res[x+1]:
            res[x], res[x+1] = res[x+1], res[x]

# res 요소를 한줄에 하나씩 출력
for i in res:
    print(i)
