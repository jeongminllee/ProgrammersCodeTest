def main() :
    n = int(input())
    bn = bin(n)[2:]
    res = []
    for idx in range(len(bn)) :
        if bn[idx] == '1' :
            res.append(len(bn) - idx - 1)
    print(*reversed(res))


if __name__ == "__main__" :
    T = int(input())
    for _ in range(T) :
        main()