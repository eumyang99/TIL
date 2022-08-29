n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

big_1 = lst[-1]                 # 가장 큰 값 찾기
big_2 = 0                       
for i in range(n-2, -1, -1):    # 두번째로 큰 값 찾기
    if lst[i] != big_1:
        big_2 = lst[i]
        break

roop, remain = divmod(m, k+1)   # 반복되는 녀석들이 몇번 반복되는지, 그리고 나머지는 얼마인지
piece = big_1*k + big_2         # 반복되는 녀석들의 합

res = piece*roop + big_1*remain 
print(res)
