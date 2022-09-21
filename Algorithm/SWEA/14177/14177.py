import sys
sys.stdin = open('input.txt')

# run 검증 함수
def runnn(hand):                                
    hand_set = set(hand)                            # set으로 중복 제거
    hand_set = list(hand_set)                       # 리스트로 바꾸고
    hand_set.sort()                                 # 정렬

    cnt = 0
    for i in range(len(hand_set)-1):            # 전체 순회를 돌면서
        if hand_set[i] + 1 == hand_set[i+1]:        # 바로 뒤에 녀석과 비교해서 +1 차이나면
            cnt += 1                                    # cnt +1
            if cnt == 2:                                    # cnt가 2이면 연달아 3개가 있는 것
                return True                                 # True 반환
        else:                                       # 1보다 큰 차이가 나면
            cnt = 0                                     # cnt는 0으로 초기화
    else:                                       # 순회가 다 끝나면
        return False                            # run이 없으니 False반환



def triplet(hand):
    hand.sort()                                     # 정렬
    idx = 0                                         # 카드 인덱스
    cnt = 0
    while idx <= len(hand)-2:                       # 카드 전체를 순회하면서    
        if hand[idx] == hand[idx+1]:                    # 다음 카드와 같은 숫자면
            cnt += 1                                        # cnt +1
            if cnt == 2:                                        # cnt가 2이면 같은 숫자 3개 있는 것
                return True                                     # True 반환
        else:                                           # 다음 카드와 다르면
            cnt = 0                                         # cnt는 0으로 초기화
        idx += 1                                        # 다음 카드 조회를 위해 idx +1
    else:                                           # 순회가 다 끝나면
        return False                                # triplet이 없으니 False반환



T = int(input())
for case in range(T):
    lst = list(map(int, input().split()))

    a = []                                  # 1번 플레이어 카드 리스트
    b = []                                  # 2번 플레이어 카드 리스트
    flag = False
    for i in range(6):
        if i <= 2:                          # 카드 3장씩 각각 넣어주고
            a.append(lst[i*2])
            b.append(lst[i*2+1])
        else:                               
            a.append(lst[i*2])              # 카드를 하나씩 넣고 
            flag = runnn(a)                 # run, triplet 검사
            if flag == True:                # True면 승자 출력 후 종료   
                print(f'#{case+1} 1')
                break
            flag = triplet(a)
            if flag == True:
                print(f'#{case+1} 1')
                break

            b.append(lst[i*2+1])
            flag = runnn(b)
            if flag == True:
                print(f'#{case+1} 2')
                break
            flag = triplet(b)
            if flag == True:
                print(f'#{case+1} 2')
                break
    else:                                   # 카드를 다 받았는데 승자가 없으면
        print(f'#{case+1} 0')               # 0 출력

