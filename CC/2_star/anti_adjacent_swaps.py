t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if (n == 2 and sorted(l) != l) or (n == 3 and l[1] != sorted(l)[1]):
        print("YES")
    else:
        print("NO")
        
# Check only for the conditions if "n" equals 2 or "n" equals 3 :

# case 1 : if n == 2 , if the given elements are not in the sorted form already , then its "NO"

# case 2 : if n == 3 , if the middle element out of the three elements is not present in its original sorted position , then its "NO"

# else , for all other cases , the result would be "YES".