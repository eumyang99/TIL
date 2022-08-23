T = int(input())
for case in range(T):
    N = int(input())
    
    # 키가 2,3,5,7,11이고 value가 0인 딕셔너리 생성
    lst = [2,3,5,7,11]
    dic = {i:0 for i in lst}
    
    # 주어진 소수들에 대해
    for i in lst:

        # 소인수분해가 끝나고 N이 1되면 그만
        if N == 1:
            break

        # N을 소수로 나눠 나머지가 0이 되면
        # N을 그 몫으로 갱신하고
        # 해당 키값의 밸류를 +1
        while 1:
            if N % i == 0:
                N = N // i
                dic[i] += 1
            # 나머지가 0이 아니면 새로운 소수로 다시 인수분해 시작
            else:
                break
    
    # 딕셔너리의 밸류들 출력
    print(f'#{case+1}', end=" ")
    for i in dic.values():
        print(i, end=" ")
    print()