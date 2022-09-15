import sys
sys.stdin = open('input.txt')

def func(node):
    if lst[node] == None:                   # 노드가 None이면
        left = node*2                           # 왼쪽 노드는 node*2
        if node*2 + 1 <= N:                     # 만약 자식 노드가 2개라면(마지막 자식 노드가 1개일 경우를 위해)    
            right = node*2 + 1                  # 오른쪽 노드는 node* + 1
            lst[node] = func(left) + func(right)# 부모 노드는 두 자식 노드의 합
            return lst[node]                    # 부모 노드 반환
        else:                                   # 마지막 자식 노드가 1개일 경우
            lst[node] = func(left)              # 부모 노드는 자식 노드와 같음
            return lst[node]                    # 부모 노드 반환
    else:                                   # 노드가 None이 아니면    
        return lst[node]                        # 해당 노드 반환



T = int(input())
for case in range(T):
    N, M, L = map(int, input().split())

    lst = [None]*(N+1)
    for _ in range(M):
        idx, value = map(int, input().split())
        lst[idx] = value

    print(f'#{case+1} {func(L)}')



T=int(input())
 
for t in range(1,T+1):
    N=int(input())                      # 자연수 개수이자 마지막 노드의 수
 
    heap=list(map(int,input().split())) # 인풋을 힙으로 사용할 거다.
    heap=[0]+heap                       # 인덱스를 맞춰주기 위해 더미 하나 추가
    for idx in range(2, len(heap)):
        while idx>=2:
            if heap[idx]<heap[idx//2]:
                heap[idx],heap[idx//2]=heap[idx//2],heap[idx]
            idx=(idx//2)
     
    sum=0
     
    nidx=N
    while nidx>=2:
        nidx=(nidx//2)
        sum+=heap[nidx]
 
    print(f'#{t} {sum}')




    