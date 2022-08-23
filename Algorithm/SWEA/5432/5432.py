T = int(input())
for case in range(T):
    lst = list(input())
    
    # '('가 등장하면 +1,
    # ')'가 등장하면 -1을 한 누적값 리스트를 생성
    # ex) ((()()))이라면 [1,2,3,2,3,2,1,0]
    # ')'괄호가 나타나면
    # 해당 인덱스의 누적값과 두칸 앞의 누적값을 비교
    # 두 값이 같으면 레이저가 발사되고, 두 값이 2차이면 쇠막대가 끝나는 것
    # 전자의 경우 누적값 만큼 쇠막대를 관통하니 result에 해당 인덱스의 누적값 추가
    # 후자의 경우 쇠막대가 닫히는 것이니 result에 +1
    result = 0 # 조각 개수
    accu = []
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
            accu.append(cnt)
        elif lst[i] == ')':
            cnt -= 1
            accu.append(cnt)
            if accu[i-2] == accu[i]:
                result += cnt
            elif accu[i-2] == accu[i]+2:
                result += 1
 
 
    print(f'#{case+1} {result}')