import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

def func(virus):
    global res
    for i in cpu[virus]:                # 함수에 입력된 virus의 밸류들에 대해
        if i not in visited:            # 방문 안했으면
            res += 1                    # res +1
            visited.add(i)              # 방문처리
            func(i)                     # 방문


n = int(input())
v = int(input())
cpu = dict()                            # 간선 정보를 저장할 dict
for i in range(1, n+1):                 # 노드 번호를 key값으로 갖는 빈 리스트를 저장
    cpu[i] = []
for i in range(v):                      # 간선 정보를 양방향으로 저장
    p, c = map(int, input().split())
    cpu[p].append(c)
    cpu[c].append(p)

res = 0                                 # 결과값 res
visited = set()                         # visited 만들고 1번 방문처리
visited.add(1)

func(1)
print(res)
        
