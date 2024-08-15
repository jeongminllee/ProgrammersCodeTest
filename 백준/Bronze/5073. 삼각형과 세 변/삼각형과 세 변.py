while True :
    try :
        a, b, c = map(int, input().split())
        if (a, b, c) == (0, 0, 0) :
            break
    except :
        break

    lst = list((a, b, c))
    lst.sort()
    a, b, c = lst
    if a + b <= c :
        print('Invalid')

    else :
        if a == b == c :
            print('Equilateral')
        elif a != b != c :
            print('Scalene')
        else :
            print('Isosceles')