import sys
input = sys.stdin.readline

## 발상
## 같은 그룹에 있는 노드끼리 연결하는 순간 사이클이 형성된다.

## 새로 배운 점
## union할 때
## parent[pe] = ps 로 하는 것 보다

# if ps < pe:
#     parent[pe]=parent[ps]
# else:
#     parent[ps]=parent[pe]

## 이렇게 하는 것이 더 효율적이다.
## find의 재귀 깊이를 줄여 주는 듯!
## 그러나 GPT는 차이가 없다고 한다.
## 하지만 전자의 경우 recursion에러가 발생하는 반면 후자는 그렇지 않다.
## 테스트 케이스의 특성일 수 있겠으나 안전한 방법으로 하자.

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(m):
    s, e = map(int, input().split())
    ps, pe = find(s), find(e)
    if ps == pe:
        print(i + 1)
        break
    if ps < pe:
        parent[pe]=parent[ps]
    else:
        parent[ps]=parent[pe]
else:
    print(0)


def union(ps, pe):
    parent[pe]=parent[ps]
