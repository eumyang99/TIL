def test(binary, k):
    for i in range(k-1):
        start = (2**i)-1
        for x in range(2**(k-2-i)):
            add = x*(2**(2+i))
            if int(binary[start + add]) == 1 or int(binary[start + 2*(start+1) + add]) == 1:
                if int(binary[start + (start+1) + add]) == 0:
                    return 0
    else:
        return 1

def solution(numbers):
    answer = []

    for num in numbers:
        k=1
        while 1:
            if 2**k-1 < len((bin(num)))-2:
                k += 1
            else:
                break


        binary = "0"*(2**k-1 - (len((bin(num)))-2))+(bin(num))[2:]
        answer.append(test(binary, k))

    return answer



