import sys
input = sys.stdin.readline

## 발상
## 콘센트에 꽂혀 있는 기기 이외의 기기를 꽂아야 할 때
## 꽂혀있는 기기 중 가장 나중에 쓰일 기기를 뽑는다

res = 0
n, k = map(int, input().split())
arr = list(map(int, input().split()))

## 꽂혀있는 기기 set
using_set = set()
## 꽂혀있는 기기 개수
using_cnt = 0

## 사용할 기기 전체를 순서대로 순회하며
for i in range(k):
    ## 꽂을 기기 번호
    device = arr[i]

    ## 1) 이미 꽂혀있으면 continue
    if device in using_set: continue

    ## 2) 콘센트 자리가 남아있으면
    if using_cnt < n:
        ## 콘센트에 꽂고
        using_set.add(device)
        ## 꽂힌 기기 개수 증가
        using_cnt += 1
        continue

    ## 3) 콘센트에서 뽑고 꽂아야 한다면
    ## 뽑을 기기 찾음
    pulled_dev, pulled_dev_idx = 0, 0
    ## 꽂힌 기기를 순회하며
    for using_dev in using_set:
        ## 이후에 언제 쓰이는지 탐색
        try:
            using_dev_next_idx = arr.index(using_dev, i+1)
        ## 이후에 쓰이지 않는다면 해당 기기를 뽑기로 결정
        except:
            pulled_dev = using_dev
            break
        
        ## 나중에 쓰이는 기기로 갱신해 나감
        if pulled_dev_idx < using_dev_next_idx:
            pulled_dev, pulled_dev_idx = using_dev, using_dev_next_idx

    ## 콘센트에서 제거 후
    using_set.remove(pulled_dev)
    ## 새로운 기기를 꽂음
    using_set.add(device)
    ## res 증가
    res += 1

print(res)

