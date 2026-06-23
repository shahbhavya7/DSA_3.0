def backtrack(i, n):
    if i < 1:
        return
    backtrack(i - 1, n)
    print(i)
    
def backtrack_rev(i, n):
    if i > n:
        return
    backtrack_rev(i + 1, n)
    print(i)
    
if __name__ == "__main__":
    backtrack(5, 1)
    backtrack_rev(1, 5)