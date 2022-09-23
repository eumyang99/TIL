import sys
sys.stdin = open('input.txt')

T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복할 때
    arr = [list(input().split()) for _ in range(4)]
 
    ans = set()
 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
 
    tmp = []
 
    for i in range(4):
        for j in range(4):
            tmp.append(arr[i][j])
            for a in range(4):
                if 0 <= i+dx[a] < 4 and 0 <= j+dy[a] < 4:
                    tmp.append(arr[i+dx[a]][j+dy[a]])
                    ai = i+dx[a]
                    aj = j+dy[a]
                    for b in range(4):
                        if 0 <= ai + dx[b] < 4 and 0 <= aj + dy[b] < 4:
                            tmp.append(arr[ai + dx[b]][aj + dy[b]])
                            bi = ai + dx[b]
                            bj = aj + dy[b]
                            for c in range(4):
                                if 0 <= bi + dx[c] < 4 and 0 <= bj + dy[c] < 4:
                                    tmp.append(arr[bi + dx[c]][bj + dy[c]])
                                    ci = bi + dx[c]
                                    cj = bj + dy[c]
                                    for d in range(4):
                                        if 0 <= ci + dx[d] < 4 and 0 <= cj + dy[d] < 4:
                                            tmp.append(arr[ci + dx[d]][cj + dy[d]])
                                            di = ci + dx[d]
                                            dj = cj + dy[d]
                                            for e in range(4):
                                                if 0 <= di + dx[e] < 4 and 0 <= dj + dy[e] < 4:
                                                    tmp.append(arr[di + dx[e]][dj + dy[e]])
                                                    ei = di + dx[e]
                                                    ej = dj + dy[e]
                                                    for f in range(4):
                                                        if 0 <= ei + dx[f] < 4 and 0 <= ej + dy[f] < 4:
                                                            tmp.append(arr[ei + dx[f]][ej + dy[f]])
                                                            ans.add(tuple(tmp))
                                                            tmp.pop()
                                                    else:
                                                        tmp.pop()
                                            else:
                                                tmp.pop()
                                    else:
                                        tmp.pop()
                            else:
                                tmp.pop()
                    else:
                        tmp.pop()
            else:
                tmp.pop()
 
    print(f'#{t+1}', len(ans))
