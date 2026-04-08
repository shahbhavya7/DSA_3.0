t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split())) 
    # sort the array in descending order
    arr.sort(reverse=True)
    total = 0
    for i in range(n - 1):
        total += arr[i]
    print(total)
    t -= 1