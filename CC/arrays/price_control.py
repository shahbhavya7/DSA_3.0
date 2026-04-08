t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    sum1 = sum(arr)
    for i in range(n):
        if arr[i] > k:
            arr[i] = k
    sum2 = sum(arr)
    print(sum1 - sum2)