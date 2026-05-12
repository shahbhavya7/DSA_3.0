import math
t = int(input())
for _ in range(t):
    x = int(input())
    temp = 10**(x-1)
    temp2 = 10**x
    for i in range(temp, temp2):
        if (i % 3 == 0 and i % 9 != 0 and i % 2 != 0):
            print(i)
            break