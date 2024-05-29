parent = [[(i, j) for j in range(51)] for i in range(51)]
board = [["" for _ in range(51)] for _ in range(51)]

def find(x, y):
    if parent[x][y] != (x, y):
        px, py = parent[x][y]
        parent[x][y] = find(px, py)
    return parent[x][y]

def solution(commands):
    answer = []
    
    for command in commands:
        order = command.split()
        if order[0] == "UPDATE":
            if len(order) == 3:
                val_1, val_2 = order[1:]
                for x in range(1, 51):
                    for y in range(1, 51):
                        if board[x][y] == val_1: board[x][y] = val_2
            elif len(order) == 4:
                r, c = map(int, order[1:3])
                val = order[3]
                px, py = find(r, c)
                board[px][py] = val
                
        
        elif order[0] == "MERGE":
            r1, c1, r2, c2 = map(int, order[1:])
            px1, py1 = find(r1, c1)
            px2, py2 = find(r2, c2)
            if (px1, py1) == (px2, py2): continue
            val_1, val_2 = board[px1][py1], board[px2][py2]
            if (val_1 and val_2) or (not val_1 and not val_2):
                board[px2][py2] = ""
                parent[px2][py2] = (px1, py1)
            elif val_1:
                parent[px2][py2] = (px1, py1)
            elif val_2:
                parent[px1][py1] = (px2, py2)   
                                
        elif order[0] == "UNMERGE":
            r, c = map(int, order[1:])
            px, py = find(r, c)
            if (r, c) != (px, py):
                board[r][c] = board[px][py]
                board[px][py] = "" 
            group = []
            for i in range(51):
                for j in range(51):
                    pi, pj  = find(i, j)
                    if (px, py) != (pi, pj): continue
                    group.append((i, j))
            for x, y in group:
                parent[x][y] = (x, y)
                                
        elif order[0] == "PRINT":
            r, c = map(int, order[1:])
            px, py = find(r, c)
            answer.append(board[px][py] if board[px][py] else "EMPTY")
    
    return answer