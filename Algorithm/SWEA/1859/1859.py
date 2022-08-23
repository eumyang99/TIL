T = int(input())
 
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    
    # 최종 출력될 결과값
    result = 0
    
    # 리스트의 최대값을 마지막 요소로 상정
    max_price = lst[-1]
    
    # 리스트의 마지막부터 처음까지
    for i in range(len(lst)-1, -1, -1):
        # 해당 요소가 마지막값보다 크면
        # 최대값을 갱신
        if lst[i] > max_price:
            max_price = lst[i]
        
        # 해당 요소가 마지막값보다 작으면
        # 최대값에서 해당 요소의 값을 빼고
        # 그 값을 result에 추가
        else:
            result += max_price-lst[i]
    print(f'#{case+1} {result}')