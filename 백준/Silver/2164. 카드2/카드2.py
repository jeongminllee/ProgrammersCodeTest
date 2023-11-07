N = int(input())
s = 2
while True :
    if (N == 1 or N == 2) :
        print(N)
        break
    s *= 2
    if s >= N :
        print((N - (s // 2)) * 2)
        break