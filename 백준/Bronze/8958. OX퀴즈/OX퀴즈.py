T = int(input())

for _ in range(T) :
    S = input()
    ans = 0
    i = 0
    for s in S :
        if s == 'O' :
            i += 1
        else :
            for num in range(1, i + 1) :
                ans += num
            i = 0

    if i != 0 :
        for num in range(1, i + 1):
            ans += num
    print(ans)