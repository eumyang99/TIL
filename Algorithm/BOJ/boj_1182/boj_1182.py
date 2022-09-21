import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

n, target = map(int, input().split())
lst = list(map(int, input().split()))

# 교수님 조합 코드 사용
def combi(idx, n, r, temp):             # idx = 현재 temp에 들어있는 원소 개수
    global cnt                          # n은 조합되는 재료 개수
                                        # r은 조합할 개수

    if idx == r:                        # 5. 만약 idx와 r이 같다면 원하는 개수가 temp 찼으니
        hap = 0                         # temp에 들어있는 조합된 녀석들을 사용함
        for i in range(r):
            hap += lst[temp[i]]
        if hap == target:
            cnt += 1
        return                          # 6. 그리고 리턴
    
    start = 0                           # 1. start = 0으로 초기설정
    if temp:                            # 2. 만약 temp에 뭐가 있으면
        start = max(temp) + 1           # 3. temp에 있는 녀석보다 +1 큰 수를 start로 설정    
                                            # 그렇지 않으면 중복되어 temp에 들어감

    for i in range(start, n):           # 4. strat부터 n까지 
        temp.append(i)                  # temp에 추가하고
        combi(idx+1, n, r, temp)        # idx를 1 높여서 다시 combi로

        temp.pop()                      # 7. 위의 함수가 return 되어 나왔으면 현재 temp는 꽉 찬 상태니까 
                                        # 마지막 한 자리를 없애고 새로운 i가 들어갈 수 있도록 자리를 마련함   

cnt = 0
for i in range(1, n+1):             # 부분수열의 크기는 1 ~ n까지
    combi(0, n, i, [])              # 각 크기에 해당하는 조합을 찾아서 사용

print(cnt)

