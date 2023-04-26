from pprint import pprint
def solution(commands):
    answer = []
    lst = [[[0,0] for _ in range(51)] for _ in range(51)]
    group_num = 1

    for words in commands:
        
        case = words.split()

        if case[0] == 'UPDATE':
            # 한 칸 배정
            if len(case) == 4:
                x1, y1 = int(case[1]), int(case[2])
                lst[x1][y1][0] = case[3]
                if lst[x1][y1][1] != 0:
                    for x in range(1, 51):
                        for y in range(1, 51):
                            if lst[x][y][1] == lst[x1][y1][1]:
                                lst[x][y][0] = case[3]
            # 앞에거를 뒤에거로 모두 바꾸기
            else:
                for x in range(1, 51):
                    for y in range(1, 51):
                        if lst[x][y][0] == case[1]:
                            lst[x][y][0] = case[2]

        elif case[0] == 'MERGE':
            x1, y1, x2, y2 = int(case[1]),int(case[2]),int(case[3]),int(case[4])
            a_value, a_group, b_value, b_group = lst[x1][y1][0], lst[x1][y1][1], lst[x2][y2][0], lst[x2][y2][1]

            if ((a_group != 0 and b_group != 0) and (a_group == b_group)) or (x1, y1) == (x2,y2):
                pass
            elif (a_value != 0 and b_value == 0):
                if a_group == 0:
                    lst[x1][y1][1] = group_num
                    if b_group == 0:
                        lst[x2][y2][0] = a_value
                        lst[x2][y2][1] = group_num
                    else:
                        for x in range(1, 51):
                            for y in range(1, 51):
                                if lst[x][y][1] == b_group:
                                    lst[x][y][0] = a_value
                                    lst[x][y][1] = group_num
                    group_num += 1
                else:
                    if b_group == 0:
                        lst[x2][y2][0] = a_value
                        lst[x2][y2][1] = a_group
                    else:
                        for x in range(1, 51):
                            for y in range(1, 51):
                                if lst[x][y][1] == b_group:
                                    lst[x][y][0] = a_value
                                    lst[x][y][1] = a_group


            elif (b_value != 0 and a_value == 0):
                if b_group == 0:
                    lst[x2][y2][1] = group_num
                    if a_group == 0:
                        lst[x1][y1][0] = b_value
                        lst[x1][y1][1] = group_num
                    else:
                        for x in range(1, 51):
                            for y in range(1, 51):
                                if lst[x][y][1] == a_group:
                                    lst[x][y][0] = b_value
                                    lst[x][y][1] = group_num
                    group_num += 1
                else:
                    if a_group == 0:
                        lst[x1][y1][0] = b_value
                        lst[x1][y1][1] = b_group
                    else:
                        for x in range(1, 51):
                            for y in range(1, 51):
                                if lst[x][y][1] == a_group:
                                    lst[x][y][0] = b_value
                                    lst[x][y][1] = b_group


            elif a_value != 0 and b_value != 0:
                if a_group == 0:
                    lst[x1][y1][1] = group_num
                    if b_group == 0:
                        lst[x2][y2][0] = a_value
                        lst[x2][y2][1] = group_num
                    else:
                        for x in range(1, 51):
                            for y in range(1, 51):
                                if lst[x][y][1] == b_group:
                                    lst[x][y][0] = a_value
                                    lst[x][y][1] = group_num
                    group_num += 1
                else:
                    if b_group == 0:
                        lst[x2][y2][0] = a_value
                        lst[x2][y2][1] = a_group
                    else:
                        for x in range(1, 51):
                            for y in range(1, 51):
                                if lst[x][y][1] == b_group:
                                    lst[x][y][0] = a_value
                                    lst[x][y][1] = a_group


            elif a_value == 0 and b_value == 0:
                if a_group == 0:
                    lst[x1][y1][1] = group_num
                    if b_group == 0:
                        lst[x2][y2][1] = group_num
                    else:
                        for x in range(1, 51):
                            for y in range(1, 51):
                                if lst[x][y][1] == b_group:
                                    lst[x][y][1] = group_num
                    group_num += 1
                else:
                    if b_group == 0:
                        lst[x2][y2][1] = a_group
                    else:
                        for x in range(1, 51):
                            for y in range(1, 51):
                                if lst[x][y][1] == b_group:
                                    lst[x][y][1] = a_group
            
        elif case[0] == 'UNMERGE':
            x1, y1 = int(case[1]), int(case[2])
            group = lst[x1][y1][1]
            
            for x in range(1, 51):
                for y in range(1, 51):
                    if lst[x][y][1] == group and group != 0 and (x,y) != (x1,y1):
                        lst[x][y][0] = 0
                        lst[x][y][1] = 0
        else:
            if lst[int(case[1])][int(case[2])][0] == 0:
                answer.append("EMPTY")
            else:
                answer.append(lst[int(case[1])][int(case[2])][0])

        # print(words)    
        # pprint(lst)
        # print()
    return answer
# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
