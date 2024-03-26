ans = 0
arr = [int(input()) for _ in range(10)]

for i in arr :
    ans += i
    if ans >= 100 :
        if abs(ans - 100) > abs(ans - i - 100) :
            ans -= i
        break
print(ans)