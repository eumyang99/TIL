import sys
sys.stdin = open("input.txt")

T = int(input())
for case in range(T):
    str1 = input()
    str2 = input()
    str1_set = set()
    for i in str1:
        str1_set.add(i)

    max_cnt = 0
    for i in str1_set:
        temp_cnt = 0
        for x in str2:
            if i == x:
                temp_cnt += 1
        if  temp_cnt > max_cnt:
            max_cnt = temp_cnt
    print(f'#{case+1} {max_cnt}')





