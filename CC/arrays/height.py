t = int(input())
for _ in range(t):
    n, x = map(int,input().split())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if arr[i] > x:
            count += 1
    print(count)