import sys
input = sys.stdin.readline


T = int(input())

if T % 10 != 0 :
    print(-1)

else :
    a, T = divmod(T, 300)
    b, T = divmod(T, 60)
    c, T = divmod(T, 10)

    print(a, b, c)