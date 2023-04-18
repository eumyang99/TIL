def test(binary, k):

    # 트리의 각 층에 대해
    for i in range(k-1):
        # start : 한 층의 맨 왼쪽 인덱스
        start = (2**i)-1
        # 한 층에 검사할 개수
        for x in range(2**(k-2-i)):
            # add : 검사할 세 개의 노드 중 가장 왼쪽 인덱스를 만들어 주는 값(start에서 더해짐)
            add = x*(2**(2+i))

            # start+1 : 세 개의 노드 간의 인덱스 간격
            left = int(binary[start + add])
            right = int(binary[start + 2*(start+1) + add])
            parent = int(binary[start + (start+1) + add])

            if left == 1 or right == 1:
                if parent == 0:
                    # 이진트리 불가능
                    return 0
    else:
        # 모든 노드를 검사했을 때 문제가 없었다면 이진트리 가능
        return 1

def solution(numbers):
    answer = []

    for num in numbers:
        # k : 트리의 높이
        k=1
        while 1:
            if 2**k-1 < len((bin(num)))-2:
                k += 1
            else:
                break

        # binary : 이진수로 변환
        binary = "0"*(2**k-1 - (len((bin(num)))-2))+(bin(num))[2:]

        # 이진수와 트리의 높이를 함수에 입력
        # 함수의 반환값을 answer에 추가
        answer.append(test(binary, k))

    return answer



