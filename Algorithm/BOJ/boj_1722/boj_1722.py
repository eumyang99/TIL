import sys
input = sys.stdin.readline

def factorial(n):
    if n >= 1 and facto[n]:
        return facto[n]
    else:
        facto[n] = n * factorial(n-1)
        return facto[n]

def func_1():
    global tg
    x = n - 1
    while 1:
        a, b = divmod(tg, factorial(x))         # tg 숫자를 한단계 낮은 팩토리얼로 나눴을 때 몫이 관건
        if b == 0:                              # 나누어 떨어지면
            print(nums.pop(a), end=" ")         # 몫에 해당하는 숫자를 출력하고 남은 숫자를 역배열로 출력
            print(*nums[-1:0:-1])
            break
        else:                                   # 나누어 떨어지지 않으면
            print(nums.pop(a+1), end=" ")       # 해당 숫자를 출력하고 나머지를 가지고 다시 낮은 팩토리얼로 나누어봄
        tg = b
        x -= 1


def func_2():                       
    global tg
    x = n - 1
    res = 0
    i = 0
    while 1:
        a = nums.index(tg[i])                   # tg의 첫번째 숫자부터 해당 숫자가 몇번째 숫자인지가 관건
        res += factorial(x) * (a-1)             # 해당 숫자의 값과 한 단계 낮은 팩토리얼을 곱했을 때 해당 숫자는 제 몫을 다함, 그 곱의 값을 res에 추가
        nums.pop(a)                             # 그리고 팝
        x -= 1                                  
        i += 1
        if x <= 1:                              # 만약 x가 1보다 작아질 경우
            if tg[i] > nums[1]:                 # 즉 숫자 한개가 남았거나 두개가 남았을 경우
                res += 2                        # 순서대로 배치되어있다면 +1을 반대로 배치되어있다면 +2를 함
                break
            else:
                res += 1
                break
    print(res)




n = int(input())
lst = list(map(int, input().split()))
if n == 1:
    print(1)
else:
    nums = [i for i in range(n+1)]
    facto = [0]*(n+1)
    facto[1] = 1
    facto[2] = 2
    if lst[0] == 1:
        tg = lst[1]
        func_1()
    else:
        tg = lst[1:]
        func_2()

