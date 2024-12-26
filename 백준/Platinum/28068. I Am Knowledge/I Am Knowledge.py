def can_read_all_books(N, happy, unhappy) :
    joy = 0

    for a, b in happy + unhappy :
        if joy < a :
            return 0
        joy -= a
        joy += b
        
    return 1
N = int(input())
happy, unhappy = [], []

for _ in range(N) :
    a, b = map(int, input().split())
    if b - a >= 0 :
        happy.append((a, b))
    else :
        unhappy.append((a, b))

happy.sort(key=lambda x:(x[0], -x[1]))
unhappy.sort(key=lambda x:(-x[1], x[0]))

print(can_read_all_books(N, happy, unhappy))