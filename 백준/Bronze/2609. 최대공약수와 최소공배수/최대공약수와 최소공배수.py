def gcd(a, b) :
    while b :
        a, b = b, a%b
    return a

def lcm(a, b) :
    res = (a * b) // gcd(a,b)
    return res

a, b = map(int, input().split())
gcd_num = gcd(a, b)
lcm_num = lcm(a, b)

print(gcd_num)
print(lcm_num)