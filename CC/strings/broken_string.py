t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n % 2 != 0:
        print("NO")
    s1 = s[:n//2] 
    s2 = s[n//2:]
    if s1 == s2:
        print("YES")
    else:
        print("NO")
    