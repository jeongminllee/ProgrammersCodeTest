def gcd(a, b) :
    while b:
        a, b = b, a%b
    return a
def lcm(a, b) :
    return abs(a * b) // gcd(a, b)

def main() :
    s = input()
    t = input()

    ls = len(s)
    lt = len(t)

    nums = lcm(ls, lt)
    if nums == -1 :
        return 0

    else :
        cnt_s = nums // ls
        cnt_t = nums // lt

        fs = s * cnt_s
        ft = t * cnt_t

        if fs == ft :
            return 1
        else :
            return 0

print(main())
