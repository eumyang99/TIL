# import sys
# sys.stdin = open('input.txt')

# T = int(input())

def binary_test(n, hex):
    data = ''
    for i in range(n):
        target = hex[i]
        if target.isdigit():
            for x in range(4-1, -1, -1):
                if int(target) & (1<<x):
                    data = data + '1'
                else:
                    data = data + '0'                    
        else:
            for x in range(4-1, -1, -1):
                if ord(target)-55 & (1<<x):
                    data = data + '1'                    
                else:
                    data = data + '0'
    data = data.rstrip('0')
    print(data)
    print(len(data))




    code_ratio = [[2,1,1], [2,2,1], [1,2,2], [4,1,1], [1,3,2], [2,3,1], [1,1,4], [3,1,2], [2,1,3], [1,1,2]]
    # code = []
    # for i in range(10):
    #     temp = ''
    #     for x in range(4):
    #         if x % 2 == 0:
    #             temp = temp + '0' * code_info[i][x]
    #         else:
    #             temp = temp + '1' * code_info[i][x]
    #     code.append(temp)

    password = []
    ratio = []
    last_idx = len(data)-1
    for i in range(last_idx-1, 0, -1):
        if data[i] != data[i+1]:
            ratio.append(last_idx-i)
            last_idx = i
            print(ratio)
            if len(ratio) % 4 == 3:
                temp = []
                for x in range(3):
                    temp.append(ratio[-1-x] // min(ratio))
                for y in range(10):
                    if code_ratio[y] == temp[::-1]:
                        password.append(y)
    password.reverse()
    print(password)
    # for i in range(len(data)%56, len(data), 7):
    #     for num in range(10):
    #         if data[i : i+7] == code[num]:
    #             password.append(num)
    #             break

    # print(password)

    # check = 0
    # for i in range(n-1):
    #     if i % 2 == 0:
    #         check += int(hex[i]) * 3
    #     else:
    #         check += int(hex[i])
    
    # res = 0
    # if check + int(hex[-1]) % 10:
    #     for i in hex:
    #         res += int(i)
    

    # return res

binary_test(len('196EBC5A316C578'), '196EBC5A316C578')







# for case in range(T):
#     n, m = map(int, input().split())
#     code = set()
#     for _ in range(n):
#         line = input().strip('0')
#         if line:
#             print(line)
#     # print(code)

