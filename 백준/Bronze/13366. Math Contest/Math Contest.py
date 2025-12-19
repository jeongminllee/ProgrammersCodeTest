T = int(input())
for _ in range(T) :
    x = input()
    sm = 0
    for i in x :
        sm += int(i)

    if sm % 9 :
        print("NO")
    else :
        print("YES")