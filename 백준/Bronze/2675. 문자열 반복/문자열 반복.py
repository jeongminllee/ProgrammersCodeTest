T = int(input())
for i in range(T) :
    R, S = map(str, input().split())
    for i in range(len(S)) :
        for _ in range(int(R)) :
            print(S[i], end = '')
    print()
    