import sys
sys.stdin = open('input.txt')

t = 10
for case in range(t):
    apt_nums = int(input())
    apt_height = list(map(int, input().split()))
    light_apt = 0
    for i in range(2, apt_nums-2):
        maxi = 0
        if apt_height[i-2] < apt_height[i] and apt_height[i-1] < apt_height[i] and apt_height[i] > apt_height[i+1] and apt_height[i] > apt_height[i+2]:
            for x in [apt_height[i-2], apt_height[i-1], apt_height[i+1], apt_height[i+2]]:
                if maxi < x:
                    maxi = x
            light = apt_height[i] - maxi
            light_apt += light

    print(f'#{case+1} {light_apt}')