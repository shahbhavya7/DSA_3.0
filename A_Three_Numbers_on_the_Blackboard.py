t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    max_num = max(a, b, c)
    min_num = min(a, b, c)
    remaining_num = a + b + c - max_num - min_num
    
    range_num = max_num - min_num
    
    if range_num > (remaining_num + min_num):
        print((remaining_num + min_num) - min_num)
    else:
        print(range_num)