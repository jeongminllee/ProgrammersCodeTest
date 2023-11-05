T = int(input())

for i in range(T) :
    o = 0
    s = 0
    lst = list(map(str, input()))
    for e in range(len(lst)) :
        if lst[e] == 'O' :
            o += 1
            s += o
        else :
            o = 0

    print(s)