# Recursion Intro
def recursion(i, n):
    if i > n:
        return
    print(i)
    recursion(i + 1, n)

#recursion(0)

def name(i,n):
    if i > n:
        return
    print("Bhavya")
    name(i + 1, n)
    
if __name__ == "__main__":
    name(1, 5)