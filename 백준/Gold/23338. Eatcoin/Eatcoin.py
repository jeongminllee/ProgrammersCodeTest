def s5(n) :
    return n * n * (n + 1) * (n + 1) * (2 * n * n + 2 * n - 1) // 12

def calc(p, q, x, n) :
    return x - n * p + q * s5(n)

p, q = map(int, input().split())

day, x = 1, -1
while True :
    if p <= q * day ** 5 :
        x = p * day - q * s5(day-1)
        break
    day += 1

print(x)

l, r = 0, 10**99
while l < r :
    m = (l + r) // 2
    if calc(p, q, x, m) >= 10 ** 99 :
        r = m
    else :
        l = m + 1
print(r)