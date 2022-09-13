import sys
input = sys.stdin.readline

def func():
    global total

    if sum(lst) <= total:                   # 모든 예산 요청 수용가능 할 때
        return max(lst)                         # 리스트의 max값 출력

    else:                                   # 그렇지 않을 때        
        cnt = 0                                 # 리스트에서 pop 되는 누적수
        mean = total // n                       # 초기 리스트의 평균값
        while 1:
            flag = False                        # 상한가로 줄 수밖에 없는 예산들만 남았을 때 false
                                                
            for i in range(n-cnt-1, -1, -1):    # 리스트 거꾸로 순회
                if lst[i] <= mean:              # 평균값보다 작은 예산이면
                    total -= lst.pop(i)         # 총예산에서 해당 값 차감
                    cnt += 1                    # 팝 횟수 +1

            mean = total // (n-cnt)             # pop되고 남은 예산들의 평균값
            for i in lst:                       # 남은 예산 순회
                if i <= mean:                   # 새로운 평균값보다 작거나 같은 예산이 있으면
                    flag = True                 # flag를 true로 바꾸고 종료 후 다시 while문으로 고고
                    break
            if flag == False:                   # 만약 flag가 여전히 false면
                return mean                     # 평균값보다 작은 예산이 없다는 뜻이니
                                                # 이 평균값이 상한액

n = int(input())
lst = list(map(int, input().split()))
total = int(input())

print(func())



