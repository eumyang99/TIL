import sys
input = sys.stdin.readline

def find(x):
    # if parent[x] != x:                        # 이렇게 하니 매번 새롭게 부모를 계속 사다리 타고 찾아가야 함
    #     return find(parent[x])
    if parent[x] != x:                          # 그래서 최종 부모의 값을 찾으면 재귀가 풀리면서 모든 자식들의 부모를 궁극적인 한 부모로 설정
        modified_parent = find(parent[x])       # 이렇게 하니 시간이 10배 가까이 줄었음...
        parent[x] = modified_parent
        return modified_parent
    return x

def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        parent[b] = a
        res[a] += res[b]

T = int(input())
for case in range(T):
    n = int(input())
    labeled_person = {}                     # 이름에 고유 숫자를 부여해서 저장
    label_num = 0                           # 고유 숫자 초기화(parent list의 인덱스 값을 의미하기도 함)
    parent = []                             # 인덱스(=자식 고유 숫자), 값(부모 고유 숫자)
    res = {}                                # 고유 숫자에 따른 출력값(네트워크 사이즈)
    for i in range(n):
        s, e = input().split()
        if s not in labeled_person:         # 첫 번째 녀석에 고유 번호가 부여되지 않았다면(아직 union된 그룹이 없는 경우)
            labeled_person[s] = label_num   # 이름에 고유 번호 부여
            parent.append(label_num)        # 인덱스와 값에 같은 labed_num을 부여(자기 자신이 부모)
            res[label_num] = 1              # 아직 형성된 네트워크가 없으니 사이즈는 1
            label_num += 1                  # 고유 번호 갱신

        if e not in labeled_person:         # 위와 동일
            labeled_person[e] = label_num
            parent.append(label_num)
            res[label_num] = 1
            label_num += 1

        union(labeled_person[s], labeled_person[e]) # 두 친구가 속한 그룹을 union

        print(res[find(labeled_person[s])]) # 어차피 s와 e는 합쳐졌으니 s의 네트워크 사이즈를 출력
        

        
