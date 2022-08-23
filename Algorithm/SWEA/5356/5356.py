T = int(input())
for case in range(T):
    lst = [input() for _ in range(5)]
 
    last_idx = []
    # 인풋되는 글자의 마지막 인덱스를 따로 기록하는 리스트를 생성 
    for i in range(5):
        last_idx.append(len(lst[i])-1)
    
    # 글자 열 중 가장 긴 길이
    max_idx = 0
    for v in last_idx:
        if v > max_idx:
            max_idx = v
 
    print(f'#{case+1}', end=" ")
    # 첫번째 열부터 가장 긴 열까지 
    for i in range(max_idx+1):
        # 모든 행에 대해
        for x in range(5):
            # 그 행이 현재 진행중인 열의 인덱스보다 작거나 같다면
            # 그 열에 글자가 존재하는 것이니까
            # 출력
            if i <= last_idx[x]:
                print(lst[x][i], end="")
    print()