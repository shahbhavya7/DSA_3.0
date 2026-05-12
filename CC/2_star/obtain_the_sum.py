t = int(input())
for _ in range(t):
    n,s = map(int,input().split())
    total  = n*(n+1)//2
    
    if total - s in range(1,n+1):
        print(total-s)
    else:
        print(-1)