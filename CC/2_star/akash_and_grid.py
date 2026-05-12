t = int(input())
for _ in range(t):
    N, xs, ys = map(int, input().split())
    
    c = (N + 1) // 2
    
    dx = abs(xs - c)
    dy = abs(ys - c)
    
    if (dx % 2) == (dy % 2):
        print(0)
    else:
        print(1)
        
