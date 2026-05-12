t = int(input())
for _ in range(t):
    a = input()
    b = input()
    a_1 = a.count('1')
    b_1 = b.count('1')
    common_1  = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            common_1 += 1
        else:
            common_1 += 0
    print(a_1, b_1, common_1)
    
# Sample Input 1
