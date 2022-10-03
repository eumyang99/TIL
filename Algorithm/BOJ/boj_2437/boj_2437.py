import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

a = 1
for i in lst:
    if i > a:
        break
    a += i
print(a)    



# # 어리석은 방법
# def test():
#     if lst[-1]-1 != 0:                  # 추의 가장 작은 무게가 1이 아니라면
#         return print(1)                     # 만들 수 없는 가장 작은 숫자는 1
#     else:                               # 그것이 아니라면
#         tg = lst[-1] + 1                # 첫 타겟이 될 숫자는 가장 작은 추 + 1이 되는 것이 합리적
#         while 1:                        # 찾을 때까지 반복
#             temp = tg                       # temp는 계산을 하기 위한 임시 타겟
#             for i in range(n):              # 리스트를 큰 숫자부터 순회하며
#                 if temp >= lst[i]:              # 만약 타겟보다 같거나 작은 숫자가 나타나면
#                     temp -= lst[i]              # temp에서 차감
#                     if not temp:                # temp가 0이 되었는지 확인하고 0이면
#                         tg += 1                 # 타겟 숫자 +1
#                         break                   # 다시 반복문으로
#             else:                           # for문을 다 돌았는데 템프가 남아있으면
#                 return print(tg)            # 타겟 출력