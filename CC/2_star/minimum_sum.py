import math
for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    gc=li[0]
    for i in range(1,n):
        gc=math.gcd(gc,li[i])
    print(gc*n)