t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    num_odd = 0
    num_even = 0
    for i in a:
        if i % 2 == 0:
            num_even += 1
        else:
            num_odd += 1
    if num_odd == 0:
        print(0)
    elif num_odd % 2 == 0:
        print(min(num_even, num_odd // 2))
    else:
        print(num_even)
    