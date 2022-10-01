import sys
sys.stdin = open('input.txt')

# 순열로 풀어보자

def permu(idx, n, temp):                    # 순열 만드는 함수를 차용
    global res
    if idx == n:                            # 조건에 맞는 순열이 만들어지면
        res += 1                            # res +1

    for i in range(n):                      
        if i not in temp:
            for x in range(len(temp)):      # 이미 temp에 들어있는 녀석과
                d = (idx-x) / (i-temp[x])   # 새로 들어갈 녀석의 기울기를 비교했을 때
                if d == 1.0 or d == -1.0:   # 1이나 -1이 아니면 대각선에 위치하지 않는 것
                    break
            else:                           # 그런 경우 순열에 추가
                temp.append(i)
                permu(idx + 1, n, temp)
                temp.pop()


T = int(input())
for case in range(T):
    n = int(input())
    res = 0
    

    for i in range(n):
        permu(1, n, [i])
    print(f'#{case+1} {res}')
                

