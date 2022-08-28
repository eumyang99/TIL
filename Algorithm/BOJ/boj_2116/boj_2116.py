import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
tb = [5, 3, 4, 1, 2, 0] # idx에 따라 마주보고 있는 녀석의 idx를 값으로 하는 리스트

res =  0
for bot in lst[0]:                      # 첫 주사위의 6개의 숫자 각각에 대해
    temp = 0
    for i in lst:                       # 각 주사위에 대해
        top = i[tb[i.index(bot)]]       # bottom 값이 주어지면 top 숫자를 도출
        if (bot == 6 and top == 5) or (bot == 5 and top == 6): # 만약 bottom과 top이 6,5로 이뤄져 있다면 +4
            temp += 4
        elif bot == 6 or top == 6:                              # 만약 bottom과 top 중에 6이 있다면 +5
            temp += 5                                           # 첫 if문에서 6,5인 경우를 걸렀으니 이렇게만 해도 됨
        else:                                                   # 그게 아닌 모든 경우에서 +6
            temp += 6
        bot = top                       # 그리고 이전 주사위의 top은 다음 주사위의 bottom이 되니까 숫자를 이전함

    if temp > res:
        res = temp

print(res)
