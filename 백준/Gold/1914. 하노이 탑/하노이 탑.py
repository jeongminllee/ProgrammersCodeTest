def hanoi(N, a, b, c):
    if N == 1 :
        print(a, c)
    else :
        hanoi(N-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(N-1, b, a, c)
        
N = int(input())
print(2**N - 1)
if N <= 20 :
    hanoi(N, 1, 2, 3)