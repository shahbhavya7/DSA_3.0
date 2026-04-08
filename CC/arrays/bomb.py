t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if arr[i] < x:
            sum += 1
            idx = i+1
    if sum == 0:
        print(0)
    else:
        print(idx)
    
# Sample Input 1
