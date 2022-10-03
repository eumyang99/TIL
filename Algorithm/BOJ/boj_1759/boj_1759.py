import sys
input = sys.stdin.readline
# idx는 temp의 길이
# n은 가용 문자의 길이
# r은 암호의 최대 길이
# temp는 암호를 담을 리스트
# start는 현재 사용가능한 문자 리스트의 시작 인덱스
# a는 사용된 모음 개수
# b는 사용된 자음 개수
def combi(idx, n, r, temp, start, a, b):                
    if idx == r:                                        # 암호가 만들어졌으면 출력
        print("".join(temp))

    for i in range(start, n):                           # 사용하지 않은 암호를 순회하며
        # 모음일 때
        if lst[i] in aeiou:                             # 추가할 문자가 모음일 때
            if l - a > 2:                               # 암호의 최대 길이에서 현재 사용된 모음의 개수를 빼고 남은 자리가 2보다 크다면(자음의 자리)
                temp.append(lst[i])                     # 암호에 추가
                combi(idx+1, n, r, temp, i+1, a+1, b)
                temp.pop()

        # 자음일 때
        else:                                           # 추가할 문자가 모음일 때
            if l - b > 1:                               # 암호의 최대 길이에서 현재 사용된 자음의 개수를 빼고 남은 자리가 1보다 크다면(모음의 자리)
                temp.append(lst[i])                     # 암호에 추가
                combi(idx+1, n, r, temp, i+1, a, b+1)
                temp.pop()

l, c = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()                              # 리스트 정렬
aeiou = {'a', 'e', 'i', 'o', 'u'}       # 모음 세트

combi(0, c, l, [], 0, 0, 0)


