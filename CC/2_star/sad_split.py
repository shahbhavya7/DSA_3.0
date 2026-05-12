t = int(input())
for _ in range(t):
    n = input()
    even = 0
    odd = 0
    for i in n:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == 0 or odd == 0:
        print("YES")
    # Need at least 2 evens to safely split
    elif even >= 2:
        print("YES")
    else:
        print("NO")