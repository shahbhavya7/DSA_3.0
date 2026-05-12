t = int(input())
vowels = set("aeiou")

for _ in range(t):
    S = input().strip()
    
    count = 0
    happy = False
    
    for ch in S:
        if ch in vowels:
            count += 1
            if count > 2:
                happy = True
                break
        else:
            count = 0
    
    print("Happy" if happy else "Sad")
    
