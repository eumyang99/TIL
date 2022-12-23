import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

res = [0] * n               # 최종 출력할 리스트

dic = defaultdict(list)

for i in range(n):          # 리스트를 순회하며
    dic[A[i]].append(i)     # 해당 숫자의 인덱스를 딕셔너리 형태로 저장

dic1 = sorted(dic.items(), key = lambda x: x[0])    # key값을 기준으로 정렬
                                                    # key = lambda x: x[0] 이것이 key값인 이유는
                                                    # 정렬 했을 때
                                                    # [(1, [1, 3, 6]), (3, [4]), (4, [0, 7]), (6, [2, 5])]
                                                    # 튜플 형식으로 리스트에 저장되기 때문에
                                                    # 튜플의 첫번째 원소인 x[0]이 키 값이 됨

val = 0
for x in dic1:              # [1,3,6] , [4] , [0,7] ... 을 순서대로 이를 인덱스 값으로 하는                                  
    for i in x[1]:          # res 리스트에 차례대로 0부터 숫자를 넣어주면 됨
        res[i] = str(val)   # STR로 저장하는 이유는 출력할 때 join함수를 쓰고 싶기 때문
        val += 1            # join함수는 문자열만 가능

print(" ".join(res))
