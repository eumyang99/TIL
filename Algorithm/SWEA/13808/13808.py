from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    V ,E = map(int, input().split())


    E_info = [[0]*V for _ in range(V)] 

    for _ in range(E):
        temp = list(map(int, input().split()))
        E_info[temp[0]-1][temp[1]-1] = 1
        E_info[temp[1]-1][temp[0]-1] = 1
    sg = list(map(int, input().split()))
    print(sg)
    pprint(E_info)
    print()
    while 1 in E_info[sg[0]]: 
        if E_info[sg[0]-1][sg[1]-1] == 1:
            print(1)
            break
        else:
            for x in range(V):
                if E_info[sg[0]][x] == 1:
                    E_info[x-1]




    