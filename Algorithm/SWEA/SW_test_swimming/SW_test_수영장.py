import sys
sys.stdin = open('input.txt')

def opti(idx, temp):            # idx는 인덱스, temp는 누적되는 비용
    global res

    if idx > 11:                # 인덱스가 초과하면
        if temp < res:          # 누적값과 res를 비교
            res = temp          # res 갱신
            return

    for i in range(idx, 12):    # 시작 idx부터 마지막까지
        a = sum(swim[i:i+3])    # i부터 3개의 누적비용을 a에 할당
        if a > m3:                  # a가 3개월 결제보다 비싸면 
            temp += m3          # temp에 3개월 비용 추가
            opti(i+3, temp)     # 그리고 이후 인덱스에 3을 추가해서 함수로
            temp -= m3          # 함수에서 빠져나오면 추가한 비용 차감하고
            temp += swim[i]     # 해당 달은 1일 결제로 처리한 뒤 다음 인덱스부터 3개월치 비교하러 for문으로
        else:                       # a가 3개월 비용보다 저렴하면
            temp += swim[i]     # 해당 월은 1일 결제로 처리
            opti(i+1, temp)     # 인덱스 +1하고 다시 함수로


            
T = int(input())
for case in range(T):
    d, m1, m3, y = list(map(int, input().split()))
    swim = list(map(int, input().split()))
    dtom = m1 // d                  # 하루 결제 보다 한달 결제가 효율적이게 되는 기준

    for i in range(12):             # 매월
        days = swim[i]              # 하루 결제가 유리하면 하루결제 비용으로
        if days > dtom:             # 한달 결제가 유리하면 한달결제 비용으로
            swim[i] = m1            # 리스트를 변경
        else:
            swim[i] = days * d

    
    res = 3000*12+1                 # 최소값을 찾으니 임의의 최대값 상정
    opti(0, 0)

    if res > y:                     # 모든 경우의 수보다 1년 결제가 효율적이면
        print(f'#{case+1} {y}')     # 1년 결제를
    else:                           # 그렇지 않다면
        print(f'#{case+1} {res}')   # 최소값을 출력

