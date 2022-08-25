import sys
input = sys.stdin.readline

T = int(input())
b = list(map(int, input().split()))


def test(lst):
    res = 0                         # 결과
    temp = 1                        # 연속된 글자 수
    flag = 0                        # 줄어들고 있는지 커가고 있는지 구분할 flag
    stack = []                      # 다른 값이 나올 때마다 해당 인덱스 append
    if len(b) == 1:                 # 리스트 길이가 1이면 그냥 1 출력
        res = 1
        return res

    for i in range(len(b)-1):       # 가장 처음 나타나는 증가 감소를 찾아 flag 설정
        if b[i] < b[i+1]:
            flag = 1
            stack.append(i)
            break
        elif b[i] > b[i+1]:
            flag = -1
            stack.append(i)
            break
    if flag == 0:                   # [0,0,0,0,0]이 주어졌을 때 for문을 다 돌아도 flag는 0
        res = len(b)                # 이런 경우는 리스트 길이를 출력
        return res


    for i in range(len(b)-1):           # 리스트를 처음부터 순회하면서
        if flag == 1:                   # 증가하고 있는 경우
            if b[i] < b[i+1]:           # 다음 숫자가 또 증가하면
                temp += 1               # temp +1
                stack.append(i)         # 다른 숫자가 나타났으니 해당 인덱스 append
            elif b[i] > b[i+1]:         # 증가하고 있었는데 감소하는 숫자가 나오면
                flag = -1               # flag -1로 바꾸고
                if res < temp:          # temp 저장
                    res = temp
                temp = i - stack.pop() + 1  # 현재 인덱스에서 마지막으로 다른 숫자가 나온 인덱스를 빼고 temp에 기록
                                            # ex) [1,1,2,2,2,0] 경우 222다음 감소하니 222만큼의 길이를 기록함
                stack.append(i)             # 다른 숫자가 나타났으니 해당 인덱스 append
            else:                           # 같은 숫자가 나오면
                temp += 1                   # temp만 +1


        elif flag == -1:                # 감소하고 있는 경우
            if b[i] > b[i+1]:           # 상동
                temp += 1
                stack.append(i)
            elif b[i] < b[i+1]:
                flag = 1
                if res < temp:
                    res = temp
                temp = i - stack.pop() + 1
                stack.append(i)
            else:
                temp += 1
    else:                               # ex) [1,0,0,0,0]로 끝났으면 temp를 기록할 수 없었으니
        if res < temp:                  # 마지막으로 기록된 temp를 res에 할당
            res = temp
    
    return res

print(test(b))


