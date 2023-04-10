def solution(cap, n, deliveries, pickups):

    answer = 0
    dStart = -1
    pStart = -1
    endIdx = 0

    for i in range(n-1, -1, -1):
        if deliveries[i] > 0:
            dStart = i
            break

    for i in range(n-1, -1, -1):
        if pickups[i] > 0:
            pStart = i
            break

    if dStart >= pStart:
        answer += 2*(dStart+1)
        endIdx = dStart
    else:
        answer += 2*(pStart+1)
        endIdx = pStart

    dCapa = cap
    pCapa = cap
    while endIdx > -1:
        if deliveries[endIdx] - dCapa  > 0 or  pickups[endIdx] - pCapa > 0:
            deliveries[endIdx] -= dCapa
            pickups[endIdx] -= pCapa
            answer += 2*(endIdx+1)
            dCapa = cap
            pCapa = cap
        else:
            dCapa -= deliveries[endIdx]
            pCapa -= pickups[endIdx]
            endIdx -= 1
    

    return answer


print(solution(2, 7, [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]))



























# def solution(cap, n, deliveries, pickups):

#     answer = 0

#     dStart = 0
#     pStart = 0
#     for i in range(n-1, -1, -1):
#         if deliveries[i] > 0:
#             dStart = i
#             break
#     for i in range(n-1, -1, -1):
#         if pickups[i] > 0:
#             pStart = i
#             break

#     if dStart >= pStart:
#         answer += 2*(dStart+1)
#     else:
#         answer += 2*(pStart+1)
    
#     while dStart != 0 or pStart != 0 :
#         dCapa = cap
#         pCapa = cap
#         for i in range(dStart,-1,-1):
#             dCapa -= deliveries[i]
#             if dCapa < 0:
#                 if dCapa == -deliveries[i]:
#                     dStart = i
#                     break
#                 else:
#                     deliveries[i] -= (cap+dCapa)
#                     dStart = i
#                     break
#             if i == 0 and dCapa >= 0:
#                 dStart = 0
#                 break
#         for i in range(pStart,-1,-1):
#             pCapa -= pickups[i]
#             if pCapa < 0:
#                 if pCapa == -pickups[i]:
#                     pStart = i
#                     break
#                 else:
#                     pickups[i] -= (cap+pCapa)
#                     pStart = i
#                     break
#             if i == 0 and pCapa >= 0:
#                 pStart = 0
#                 break
        
#         if dStart >= pStart:
#             answer += 2*(dStart+1)
#         else:
#             answer += 2*(pStart+1)

#     return answer


# print(solution(	2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))