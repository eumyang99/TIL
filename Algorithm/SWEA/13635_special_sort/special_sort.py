import sys
sys.stdin = open("input.txt")

T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    # 최대값 구하는 함수
    def my_max(lst):
        temp = lst[0]
        for i in range(len(lst)):
            if lst[i] > temp:
                temp=lst[i]
        return temp
    
    # 최소값 구하는 함수
    def my_min(lst):
        temp = lst[0]
        for i in range(len(lst)):
            if lst[i] < temp:
                temp=lst[i]
        return temp

    # 빈 리스트를 만들고
    res = []

    # res 리스트의 원소 길이가 10에 도달하면 그만
    while len(res) < 10:
        # 리스트의 최대값을 찾아서 res에 추가
        # 그 최대값은 리스트에서 제거
        max_value = my_max(lst)
        res.append(max_value)
        lst.remove(max_value)

        # 리스트에 최소값을 찾아서 res에 추가 
        # 그 최소값은 리스트에서 제거
        min_value = my_min(lst)
        res.append(min_value)
        lst.remove(min_value)

    print(f'#{case+1} {" ".join(map(str, res))}')




# lst = [1,2,3,4,5,6,7,8,9,10]

# max_5 = []
# mix_5 = []

# max_temp = lst[0]
# min_temp = lst[0]
# for i in range(1, len(lst)):
#     if lst[i] > max_temp:
#         max_temp = lst[i]
#     if lst[i] <min_temp:
#         min_temp = lst[i]
