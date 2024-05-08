N = int(input())
arr = list(map(int, input().split()))
ans = 1
s = ans

for i in range(N-1) :
    ans = min(ans+1, arr[-2-i])
    s += ans

print(s)