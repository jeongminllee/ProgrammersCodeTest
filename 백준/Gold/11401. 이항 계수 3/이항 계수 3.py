n, k = map(int, input().split())

mod = 1_000_000_007

def binomial(n1, n2, p) :
    def pow(x, pp) :
        if pp < 3 :
            if pp == 2 :
                return (x**2) % p
            if pp == 1 :
                return x % p
        if pp % 2 == 0 :
            return (pow(x, pp//2)**2)%p
        return ((pow(x, (pp-1)//2)**2)*x)%p
    return (n1 * pow(n2, p-2)) % p

k = min(n-k, k)
n1 = n
n2 = 1

for i in range(2, k + 1) :
    n1 *= (n - i + 1)
    n2 *= i
    n1 %= mod
    n2 %= mod

res = binomial(n1, n2, mod)

if k == 0 :
    res = 1

print(res % mod)