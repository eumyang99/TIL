import sys
input = sys.stdin.readline

## 발상
## '-'를 처음 만나기 전까지의 모든 숫자들의 합에서 이후에 나오는 모든 숫자들을 빼면 된다.
## '-'를 처음 만나기 전     => flag가 True 
## '-'를 처음 만난 이후     => flag가 False
## 부호를 만나는 순간들을 체크해서 left pointer, right pointer를 사용
## 두 포인터 간의 숫자를 res에 더하거나 뺐다.


line = input().rstrip()
len = len(line)

res = 0
flag = True
left, right = -1, -1

for i in range(len):
    right = i
    if flag == True:
        if line[right] == '+' or line[right] == '-':
            res += int(line[left+1:right])
            left = i
            if line[right] == '-':
                flag = False
        
    else:
        if line[right] == '+' or line[right] == '-':
            res -= int(line[left+1:right])
            left = i

else:
    if flag == True:
        res += int(line[left+1:])
    else:
        res -= int(line[left+1:])
    
print(res)

