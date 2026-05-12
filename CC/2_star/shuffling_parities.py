t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    even_on_even = 0
    odd_on_odd = 0
    
    for i in range(n):
        if a[i] % 2 == 0 and (i + 1) % 2 == 0:
            even_on_even += 1
        elif a[i] % 2 == 1 and (i + 1) % 2 == 1:
            odd_on_odd += 1
    
    if abs(even_on_even - odd_on_odd) == 0:
        print(len(a))
    else:
        print(len(a) - abs(even_on_even - odd_on_odd))