t = int(input())
for _ in range(t):
    X = int(input())
    s = input()
    chef = 0
    carlsen = 0
    draw = 0
    for i in range(s.__len__()):
        if s[i] == 'N':
            chef += 1
        elif s[i] == 'C':
            carlsen += 1
        else:
            draw += 1
    chef_score = draw * 1 + chef * 2
    carlsen_score = draw * 1 + carlsen * 2
    if chef_score > carlsen_score:
        money = 40 * X
        print(money)
    elif carlsen_score > chef_score:
        money = 60 * X
        print(money)
    else:
        money = 55 * X
        print(money)