def gcd(a:int, b:int) :
    if a == 0 :
        return b
    elif b == 0 :
        return a
    else :
        return gcd(b, a%b)
    

def main() :
    x, y = map(int, input().split())
    x = abs(x)
    y = abs(y)

    g = min(gcd(x, y), 2)

    print(g)
        
main()