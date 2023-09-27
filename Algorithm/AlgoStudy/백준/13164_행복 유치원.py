import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

gap = []
for i in range(n-1):
    gap.append(arr[i+1] - arr[i])
gap.sort()

print(sum(gap[:n-k]))