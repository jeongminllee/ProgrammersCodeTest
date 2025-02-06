def main() :
    n = int(input())
    a, b = 0, 1

    for _ in range(n) :
        a, b = b, (a+b) % 1_000_000_007
    print(a)



main()