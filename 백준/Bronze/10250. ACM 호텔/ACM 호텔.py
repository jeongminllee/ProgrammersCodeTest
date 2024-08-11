T = int(input())

for _ in range(T) :
    H, W, N = map(int, input().split())
    if N % H == 0 :
        print(H * 100 + N // H)
    else :
        print(N%H * 100 + N // H + 1)
        
'''
T = int(input())

for _ in range(T) :
    H, W, N = map(int, input().split())
    ans = 101
    while N > 0 :
        if N > H :
            N -= H
            ans += 1

        else :
            ans += (N-1) * 100
            N = 0

    print(ans)
'''

