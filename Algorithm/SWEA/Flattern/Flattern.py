import sys
sys.stdin = open('input.txt')
# sort를 쓰지 않고 풀어봄 (카운팅 정렬 사용)
# for case in range(10):
#     chances = int(input())
#     height = list(map(int, input().split()))
 
 
#     cnt = [0]*101
#     lst = [0]*len(height)
 
#     for i in height:
#         cnt[i] +=1
 
#     for i in range(1, len(cnt)):
#         cnt[i] += cnt[i-1]
 
#     for i in height[::-1]:
#         lst[cnt[i]-1] = i
#         cnt[i] -= 1
#     height = lst
 
 
#     for i in range(chances):
#         height[0] += 1
#         height[-1] -= 1
 
#         cnt = [0]*101
#         lst = [0]*len(height)
#         for i in height:
#             cnt[i] +=1
#         for i in range(1, len(cnt)):
#             cnt[i] += cnt[i-1]
#         for i in height[::-1]:
#             lst[cnt[i]-1] = i
#             cnt[i] -= 1
#         height = lst
 
#     print(f'#{case+1} {height[-1]-height[0]}')

for test_case in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    k = 0
    while k < dump:
        min_i = 0
        max_i = 0
        for i in range(1, 100):
            if lst[i] < lst[min_i]:
                min_i = i
            if lst[i] > lst[max_i]:
                max_i = i


        if lst[max_i] - lst[min_i] > 1:
            lst[min_i] += 1
            lst[max_i] -= 1
            k += 1
        else:
            break

    print(f'#{test_case} {lst[max_i] - lst[min_i]}')