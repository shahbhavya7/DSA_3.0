t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dic = {}
    a = True   
    for i in range(2*n):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    for key in dic: #
        if dic[key] > 2:
            a = False
    if a:
        print("YES")
    else:
        print("NO")