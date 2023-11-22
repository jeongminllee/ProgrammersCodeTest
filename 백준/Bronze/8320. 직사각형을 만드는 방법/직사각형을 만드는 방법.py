N = int(input())
ans = N
for i in range(2, N) :
    n = N // i - (i - 1)
    if n < 1 :
        break
    ans += n
print(ans)