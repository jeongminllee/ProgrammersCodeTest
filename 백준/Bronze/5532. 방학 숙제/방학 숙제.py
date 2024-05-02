lst = []
for _ in range(5) :
    i = int(input())
    lst.append(i)

l, a, b, c, d = lst
ans = max(a//c+(1 if a%c else 0), b//d+(1 if b%d else 0))
print(l - ans)