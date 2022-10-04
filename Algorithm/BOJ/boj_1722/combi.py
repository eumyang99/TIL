def combi(idx, n, temp):
    if idx == n:
        print(temp)
        return

    for i in range(1, n+1):
        if i not in temp:
            temp.append(i)
            combi(idx+1, n, temp)
            temp.pop()
    if idx == 1:
        print()


combi(0, 4, [])