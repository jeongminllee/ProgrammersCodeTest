import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N) :
    a = input().rstrip()
    if 'push' in a :
        lst.append(a.split()[1])

    elif 'pop' in a :
        if len(lst) == 0 :
            print(-1)
        else :
            print(lst.pop(0))

    elif 'size' in a :
        print(len(lst))

    elif 'empty' in a :
        if len(lst) == 0 :
            print(1)
        else :
            print(0)

    elif 'front' in a :
        if len(lst) == 0 :
            print(-1)
        else :
            print(lst[0])
    else :
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])