import sys
input = sys.stdin.readline

def counting(m, arr, len):
    cnt = 0
    idx = len-1
    if len:
        while idx >= 0:
            cnt += arr[idx]*2
            idx -= m
        else:
            return cnt
    else:
        return 0


n, m = map(int, input().split())
lst  = list(map(int, input().split()))
left, right = [], []
for loca in lst:
    if loca < 0:
        left.append(-loca)
    else:
        right.append(loca)
left.sort()
right.sort()

left_len = len(left)
right_len = len(right)

res = 0
res += counting(m, left, left_len)
res += counting(m, right, right_len)

if left_len:
    left_max = max(left)
else:
    left_max = 0
if right_len:
    right_max = max(right)
else:
    right_max = 0
res -= max(left_max, right_max)
print(res)

## 다른 사람 코드
## 미쳤네... 코드를 무한 줄이는 구나
## 배울점 1
  ## sorted(list(map(int, input().split())))
  ## input 받으면서 바로 sort 하기
## 배울점 2
  ## left[::M]
  ## idx 0번부터 끝까지 0, m, 2m, 3m, 4m ... 인덱스 값을 불러올 수 있음
  ## 만약 저렇게 가다가 인덱스가 초과하면 그냥 마지막 값을 불러옴
## 배울점 3
  ## 나는 left와 right가 비어있을 때 그 길이로 분기처리를 했는데
  ## max(left + right) 이 사람은 left와 right 인덱스를 합치고 거기서 max값을 찾음... ㄷㄷㄷ

## 할 말이 없네............

N, M = map(int, input().split())
books = sorted(list(map(int, input().split())))

left = []
right= []
for book in books:
    if book < 0:
        left.append(-book)
    else:
        right.append(book)

right.reverse()

print((sum(left[::M]) + sum(right[::M])) * 2 - max(left + right))