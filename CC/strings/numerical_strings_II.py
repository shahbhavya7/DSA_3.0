t = int(input())
for _ in range(t):
    n = int(input())
    string1 = str(n)
    # find 5 in string1
    if string1 == string1[::-1]:
        print("YES")
    else:
        print("NO")