# 8*8을 쭉 돌면서 wb, bw 패턴을 체크
# 일일이 비교해보면서 다른 글자의 숫자를 카운트
# 다른 숫자의 카운트가 작을 수록 res값 갱신

def func(x, y):
    pt_1 = 'WBWBWBWB'
    pt_2 = 'BWBWBWBW'

    cnt_1 = 0                               ### 1) 'WBWBWBWB' 'BWBWBWBW'               
    for p in range(x, x+8):                 # 틀린 글자 찾을 때마다 cnt +1
        if not p%2:
            for q in range(y, y+8):
                if lst[p][q] != pt_1[q-y]:
                    cnt_1 += 1
        else:
            for q in range(y, y+8):
                if lst[p][q] != pt_2[q-y]:
                    cnt_1 += 1
            
    cnt_2 = 0                               ### 1)  'BWBWBWBW' 'WBWBWBWB'
    for p in range(x, x+8):                 # 틀린 글자 찾을 때마다 cnt +1
        if p%2:
            for q in range(y, y+8):
                if lst[p][q] != pt_1[q-y]:
                    cnt_2 += 1
        else:
            for q in range(y, y+8):
                if lst[p][q] != pt_2[q-y]:
                    cnt_2 += 1

    if cnt_1 < cnt_2:                       # 두 패턴 중 작은 것을 반환
        return cnt_1
    else:
        return cnt_2



import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
lst = [input() for _ in range(m)]

res = m*n
for x in range(m-7):
    for y in range(n-7):
        temp = func(x, y)
        if temp < res:
            res = temp

print(res)


