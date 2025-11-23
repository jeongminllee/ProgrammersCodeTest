def dc(k, l, n) :
    if n <= 3 :
        return 'm' if n == 1 else 'o'
    center = k + 3
    left = (l - center) // 2
    if n <= left:
        return dc(k-1, left, n)
    elif n > (left + center) :
        return dc(k-1, left, n - (left + center))
    else :
        return ('m' if left + 1 == n else "o")

def main() :
    n = int(input())
    l = 3
    k = 1

    while True :
        l = 2 * l + k + 3
        if l > n :
            break
        k += 1
    print(dc(k, l, n))

if __name__ == "__main__" :
    main()