N, B = input().split()
N = N[::-1]
B = int(B)
res = 0
for i in range(len(N)) :
    n = N[i]
    if n.isdigit() :
        n = int(n)
    else :
        n = ord(n) - ord("A") + 10

    res += n * (B ** i)

print(res)