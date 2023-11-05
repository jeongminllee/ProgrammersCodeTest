N = int(input())
N_input = N
x = []
x.append(N)
while True :
    a = N // 10
    b = N % 10
    c = (a + b) % 10
    d = b * 10 + c
    if d == N_input :
        print(len(x))
        break
    else :
        x.append(d)
        N = d