def main() :
    a = b = 0
    while True :
        try :
            n = int(input())
            a += n
            b += n
            if a > 100 :
                a -= n
                break

        except :
            break
    if abs(a - 100) >= abs(b - 100) :
        print(b)
    else :
        print(a)

if __name__ == "__main__" :
    main()