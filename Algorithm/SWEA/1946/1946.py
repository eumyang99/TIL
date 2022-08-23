import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, (T + 1)):
    # 압축 푼 str 저장할 빈 공간 생성
    result = ''
    # 먼저 인풋 받은 숫자 만큼 반복
    for k in range(int(input())):
        # 'A 10'일 경우 word와 number에 str 형태로 따로 'A'와 '10'을 할당
        word, number = map(str, input().split())
        # number을 int로 바꾸어 해당 number만큼 word를 result에 저장
        result += word * int(number)

    # 케이스 출력
    print(f'#{case}')
    # 임시 temp 만들고
    temp = ''
    # result의 문자를 특정할 idx 0부터
    idx = 0
    # idx가 마지막 글자의 인덱스보다 작을 동안 반복
    while idx <= len(result)-1:
        # temp에 해당 idx 문자 추가
        temp += result[idx]
        # idx += 1
        idx += 1
        # 만약 temp의 길이가 10이되면
        # temp를 출력하고 temp를 비움
        if len(temp) == 10:
            print(temp)
            temp = ''
    # while이 다 돌았을 때 temp 길이가 10이 안되어 있을 수 있으니
    # 남은 녀석들 출력
    else:
        print(temp)
