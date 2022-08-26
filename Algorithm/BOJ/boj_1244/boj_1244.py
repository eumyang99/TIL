import sys
input = sys.stdin.readline

size = int(input())
light = [2] + list(map(int, input().split()))                   # 인덱스 편의상 전구 리스트 맨 앞에 더미 2 추가

num = int(input())
lst = [list(map(int, input().split())) for i in range(num)]     # 학생 정보 리스트


for i in range(num):
    mw = lst[i][0]                      # 성별 구분
    idx = lst[i][1]                     # 해당 학생의 idx
    # 남학생
    if mw == 1:
        m_idx = idx                     # idx의 배수가 될 m_idx
        while m_idx <= size:            # m_idx가 전구 리스트 사이즈보다 작다면
            if light[m_idx] == 0:       # 전구 상태 변화
                light[m_idx] = 1
            elif light[m_idx] == 1:
                light[m_idx] = 0
            m_idx += idx                # 전구 다 바꾸고 m_idx에 idx의 다음 배수 할당



    # 여학생
    elif mw == 2:
        if light[idx] == 0:             # 가장 먼저, 받은 idx의 전구 상태 변화
            light[idx] = 1
        elif light[idx] == 1:
            light[idx] = 0

        if idx == 1 or idx == size:     # 받은 idx가 전구리스트의 처음이나 끝이라면 더 이상 작업은 불가, 다음 학생으로
            continue

        L_idx = idx-1                   # 양쪽 검사할 L_idx와 R_idx
        R_idx = idx+1
        while R_idx <= size and light[L_idx] == light[R_idx]:   # R_idx가 리스트를 넘지 않으면서
            if light[L_idx] == 0:                               # L과 R의 전구 상태가 같다면
                light[L_idx] = 1                                # 전구 상태 변화
                light[R_idx] = 1
            elif light[L_idx] == 1:
                light[L_idx] = 0
                light[R_idx] = 0
            L_idx -= 1                                          # L_idx, R_idx를 한 칸 더 양쪽으로 옮김
            R_idx += 1

light.pop(0)                            # 더미로 넣었던 처음 2를 빼고
for i in range(size):
    if i != 0 and i % 20 == 0:          # 20번 출력하면 줄바꿈
        print()
    print(light[i], end=" ")


