from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_sum = arr[0] + arr[n-1]
    for i in range(n-1):
        sum  = arr[i] + arr[i+1]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)
    