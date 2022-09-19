import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    lst = []
    for _ in range(n):                  # 어차피 직사각형을 이루는 가로줄을 다 같기 때문에
        a = list(map(int, input()))     # 가로줄 하나만 받아서 분석하려고 함
        if not lst and 1 in a:          # 저장할 리스트가 비어 있고 해당 가로줄에 1이 들어 있으면  
            lst = a                     # 리스트에 저장

    # 코드 정보 저장
    code_info = [[3,2,1,1], [2,2,2,1], [2,1,2,2], [1,4,1,1], [1,1,3,2], [1,2,3,1], [1,1,1,4], [1,3,1,2], [1,2,1,3], [3,1,1,2]]
    # 코드 정보 패턴에 매핑되는 암호 값을 idx로 하는 리스트로 저장
    code = []
    for i in range(10):
        temp = []
        for x in range(4):
            if x % 2 == 0:
                temp += [0] * code_info[i][x]
            else:
                temp += [1] * code_info[i][x]
        code.append(temp)


    password = []
    for i in range(m-1, -1, -1):                        # 받은 가로줄에서 
        if lst[i] == 1:                                 # 거꾸로 순회하며 1이 찾아지면
            for i in range(i-55, i, 7):                 # 그로부터 앞으로 56번째부터 7개 단위로 패턴 검사
                for num in range(10):                   
                    if lst[i : i+7] == code[num]:       # 패턴을 찾으면 패턴에 매핑되는 숫자를 password에 저장 
                        password.append(num)
                        break
            break

    check = 0                                           # 10의 배수인지 확인하는 값
    res = 0                                             # 출력할 값
    for i in range(8):                                  # password에 저장된 8자리 수를 순회하면서
        if i % 2 == 0:
            check += password[i] * 3                    # 홀수번째 수는 3을 곱해서 check에 더하고
            res += password[i]                          # res에는 그냥 더하고
        else:
            check += password[i]                        # 짝수번째 수는 그냥 check에 더하고
            res += password[i]                          # res에는 그냥 더하고
    
    if check % 10 == 0:                                 # check이 10의 배수면
        print(f'#{case+1} {res}')                       # res 출력
    else:
        print(f'#{case+1} 0')

        