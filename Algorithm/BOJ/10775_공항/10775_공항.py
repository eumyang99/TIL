import sys
input = sys.stdin.readline

## 백준에서 순위권에 드는 풀이법을 보면 비행기를 정착하는 리스트를 만들지 않는다.
## 또한 union-find를 응용해서 find만 활용한다.
## 이 과정에서 부모를 찾아가는 깊이를 줄여 속도가 더 빠르게 해결한다.
## 메모리도 속도도 코드도 훨씬 효율적이다.
## find의 재귀활용법이 매우 헷갈린다.

## 예시코드
# import sys
# input = sys.stdin.readline

# gate = int(input())
# planes = [int(input()) for _ in range(int(input()))]

# parent = [i for i in range(gate + 1)]

## 이 부분이 어려운 부분
# def find(a):
#     if a == parent[a]:
#         return a
#     parent[a] = find(parent[a])
#     return parent[a]


# answer = 0
# for plane in planes:
#     temp = find(plane)
#     if temp == 0:
#         break
#     parent[temp] = parent[temp - 1]
#     answer += 1

# print(answer)

################################################################################################
## 아래는 내 풀이법

## 발상
## 비행기를 정착할 리스트 마련(port) -> 게이트 번호는 idx, 값은 비행기 번호
## 비행기를 정착할 게이트 번호 리스트 마련(goto) -> 비행기 번호는 idx, 값은 정착할 게이트 번호
## port에 자리가 비어있으면(값이 False) 비행기 넣어줌
## port에 자리가 없으면 그 자리에 정착한 비행기 번호를 찾아서
## goto에서 조회, 해당 비행기는 어떤 번호로 가야 하는지 추적한다.
## 이 과정을 반복해서 port에 자리가 비어있으면 정착시킨다.
## 정착을 시키면서 비어있는 자리로 유도한 바로 전 비행기의 goto값을 찾아 그것보다 -1을 해준다.
## 예를 들어 4, 4, 3번 비행기가 왔다면
## 처음 4번 goto는 4 -> 3
## 두번째 4번 goto는 3 -> 2
## 세번째 3번 goto는 여전히 3이지만 이미 3번 게이트는 4번 비행기가 차지하고 있다.
## 4번 비행기의 현재 goto는 2이기 때문에 3번은 2번으로 정착시키고
## 3번 비행기의 goto는 4번 비행기의 goto인 2번 게이트에서 -1을 해서 1로 만든다.

## 예시 1)
## 이후 다시 4번 비행기가 왔다면 4번 비행기의 goto는 2번 게이트인데 2번 게이트에는 3번 비행기가 차지하고 있기 때문에
## 3번 비행기의 goto인 1번 게이트로 보낸다.
## 그리고 4번 비행기의 goto는 3번 비행기의 goto에서 -1을 해서 0으로 만든다.
## 이후 1번 비행기가 왔다면 1번 비행기의 goto인 1번 게이트는 4번 비행기가 차지하고 있기 때문에
## 4번 비행기의 goto인 0번으로 보낸다. 0번 게이트로 보내야 한다는 것은 자리가 없다는 뜻으로 종료한다.

## 예시 2)
## 이후 2번 비행기가 왔다면 2번 비행기의 goto인 2번 게이트는 3번 비행기가 차지하고 있기 때문에
## 3번 비행기의 goto인 1번 게이트로 보낸다.
## 그리고 2번 비행기의 goto는 3번 비행기의 goto에서 -1을 해서 0으로 만든다.
## 이후 1~4번 비행기가 오면 결국 0번 게이트로 보내게 되기 때문에 종료한다.

def landing(plane):
    go = goto[plane]
    while 1:
        if go == 0:
            return "stop"
        else:
            if port[go] == False:
                port[go] = plane
                goto[plane] = go-1
                break
            else:
                go = goto[port[go]]

g = int(input())
p = int(input())

port = [False for _ in range(g+1)]
goto = [i for i in range(g+1)]
res = 0

for _ in range(p):
    plane = int(input())
    if landing(plane) == "stop":
        break
    else:
        res += 1

print(res)




# 20
# 20
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 15
# 15
# 15
# 15
# 15
# 15
# 6
# 1
# 16
# 17
# 15
# 15
# 15






# 20
# 20
# 7
# 12
# 1
# 14
# 5
# 6
# 15
# 20
# 10
# 4
# 9
# 8
# 3
# 13
# 2
# 11
# 17
# 19
# 16
# 18