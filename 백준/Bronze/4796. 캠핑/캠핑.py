cnt = 0
while True :
    cnt += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0 :
        break

    a = (V // P) * L
    b = min((V % P), L)

    print("Case %d: %d" %(cnt, a + b))