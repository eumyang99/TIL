import sys
sys.stdin = open('input.txt')

def func(x):
    return (x[0],-x[1])
    # return (-x[0],x[1])
T = int(input())
for case in range(T):
    d, m1, m3, m12 = list(map(int, input().split()))
    swim = list(map(int, input().split()))

    temp_1 = [0]*12
    for i in range(12):
        if swim[i] > m1 / d:
            temp_1[i] = m1
        else:
            temp_1[i] = d*swim[i]
    
    print(temp_1)


    idx = 0
    while idx < 12:
        temp = 0
        if idx <= 12-5:
            for x in range(3):
                if x == 0:
                    if temp > m3:
                        temp = sum(temp_1[idx+x:idx+3+x])
                    else:
                        idx += 1
                        break
                else:
                    if temp < sum(temp_1[idx+x:idx+3+x]):
                        idx += 1
                        break
            else:
                for p in range(3):
                    if p == 0:
                        temp_1[idx] = temp
                    else:
                        temp_1[idx+p] = 0
                idx += 3
                break
        else:
            break
        







        
            

    print(f'#{case+1} {temp_1}')
    res = sum(temp_1)
    if res < m12:
        print(f'#{case+1} {sum(temp_1)}')
    else:
        print(f'#{case+1} {m12}')
    print()

