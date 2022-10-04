import sys
input = sys.stdin.readline
# 애초에 백색과 흑색은 서로 공격을 못함
# 그렇기 때문에 백색 자리를 검증할 때 흑색은 검증할 필요가 없음
# 따라서 비효율적인 검증을 배제하기 위해
# 흑색은 흑색끼리, 백색은 백색끼리 해서
# 시간복잡도를 n! 에서 2*(n/2)!으로 줄일 수 있다



# 흑색만 검사
def permu_1(temp_1, start_x):
    global res_1
    for i in range(start_x, len(pan_1)):                # pan_1에 있는 녀석들을 순회하며
        if pan_1[i][2] == 1:                            # 비숍을 놓을 수 있는 자리이면
            if temp_1:                                  
                for x in temp_1:                        # temp_1에 들어 있는 녀석들과 기울기 비교를 해서
                    dx = (pan_1[i][0] - x[0])
                    dy = (pan_1[i][1] - x[1])
                    if dy != 0:                         # 같은 행에 없으면서
                        if dx/dy == 1 or dx/dy == -1:   # 대각선 상에 있으면
                            break                       # 다음 자리 탐색
                    else:                               # 같은 행에 있으면
                        continue                        # 다음 비숍과 비교
                else:                                   # 위 검증이 다 끝나서 문제가 없는 자리면
                    temp_1.append(pan_1[i])             # 비숍을 놓고
                    permu_1(temp_1, i+1)                # 다음으로 비숍을 놓을 자리를 탐색하러 재귀
                    temp_1.pop()                        # 위 함수가 끝났으면 pop

            else:                                       # 애초에 temp_1이 비어있으면 그냥 놓기
                temp_1.append(pan_1[i])
                permu_1(temp_1, i+1)
                temp_1.pop()

    else:                                               # 마지막 자리까지 탐색이 끝났을 때
        if len(temp_1)> res_1:                          # temp에 있는 녀석들의 수를
            res_1 = len(temp_1)                         # res_1에 갱신
            return


# 백색만 검사       
def permu_2(temp_2, start_x):                           # 백색도 흑색과 같은 로직
    global res_2
    for i in range(start_x, len(pan_2)):
        if pan_2[i][2] == 1:
            if temp_2:
                for x in temp_2:
                    dx = (pan_2[i][0] - x[0])
                    dy = (pan_2[i][1] - x[1])
                    if dy != 0:
                        if dx/dy == 1 or dx/dy == -1:
                            break
                    else:
                        continue
                else:
                    temp_2.append(pan_2[i])
                    permu_2(temp_2, i+1)
                    temp_2.pop()
            else:
                temp_2.append(pan_2[i])
                permu_2(temp_2, i+1)
                temp_2.pop()
    else:
        if len(temp_2) > res_2:
            res_2 = len(temp_2)
            return

# pan_1 에는 흑색만 담고
# pan_2 에는 백색만 담는다
# 담는 내용은 행의 값과 열의 값, 1or0
n = int(input())
lst = []
pan_1 = []
pan_2 = []
for x in range(n):
    lst = list(map(int, input().split()))
    if x % 2 == 0: 
        for i in range(n):
            if i % 2 == 0:
                pan_1.append((x, i%n, lst[i]))
            else:
                pan_2.append((x, i%n, lst[i]))
    else:
        for i in range(n):
            if i % 2 == 1:
                pan_1.append((x, i%n, lst[i]))
            else:
                pan_2.append((x, i%n, lst[i]))


res_1 = 0
res_2 = 0
permu_1([], 0)          # 흑색 검사
permu_2([], 0)          # 백색 검사
print(res_1 + res_2)    # 흑색 최대 개수 + 백색 최대 개수 출력

