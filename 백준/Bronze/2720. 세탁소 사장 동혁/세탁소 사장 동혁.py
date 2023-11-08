import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    coin = [0] * 4
    N = int(input())
    while N != 0 :
        if N >= 25 :
            N -= 25
            coin[0] += 1

        elif N >= 10 :
            N -= 10
            coin[1] += 1

        elif N >= 5 :
            N -= 5
            coin[2] += 1

        elif N >= 1 :
            N -= 1
            coin[3] += 1
    print(coin[0], coin[1], coin[2], coin[3])