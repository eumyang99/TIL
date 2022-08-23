import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    str1 = input()
    str2 = input()
 
    
    # 보이어 무어 활용

    # 긴 문자열(비교 당하는)의 인덱스 j
    # 짧은 문자열(패턴)의 인덱스 i
    j = len(str1) - 1
    i = len(str1) - 1
    
    # 보이어 무어는 뒷글자부터 비교하기 때문에
    # j가 str2의 인덱스를 넘어가기 전까지 반복
    while j < len(str2):
        # 만약 맨 뒷글자가 같다면
        # j와 i를 -1씩해서 바로 앞글자를 비교
        if str2[j] == str1[i]:
            i -= 1
            j -= 1
            # 패턴과 모든 글자가 같으면 i는 계속 감소하다가 -1이 되는데
            # 그렇다면 패턴이 있다는 것이니까 1을 출력하고 그만 
            if i < 0:
                print(f'#{case+1} 1')
                break
        
        # 비교하는 글자가 같지 않다면
        else:
            # 패턴의 맨 마지막에서 바로 앞글자부터 첫글자까지
            for x in range(len(str1)-2, -1, -1):
                # 가장 최근 같지 않았던 str1의 글자와 비교해서
                # 만약 같은 글자가 찾아지면 다시 그 글자와
                # 가장 최근 같지 않았던 str1의 글자의 인덱스를 조절해서
                # 처음 while문으로 돌려보냄
                if str2[j] == str1[x]:
                    j += len(str1)-x-1
                    i = len(str1) - 1
                    break
            # 위의 for문을 다 돌았는데 패턴 안에 해당 글자가 없다면
            # 패턴 글자(str1)의 길이만큼 j의 인덱스를 조정
            else:
                j += len(str1)
    # J의 인덱스가 str2의 길이를 넘어서서 while문이 종료됐다면
    # 같은 패턴이 없다는 뜻이니 0을 출력하고 종료
    else:
        print(f'#{case+1} 0')