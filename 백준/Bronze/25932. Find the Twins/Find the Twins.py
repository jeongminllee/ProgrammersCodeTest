def main() :
    """
    Mack = 18
    Zack = 17
    """
    n = int(input())
    for _ in range(n) :
        lst = list(map(int, input().split()))
        lst_set = set(lst)
        print(*lst)
        if 18 in lst_set :
            if 17 in lst_set :
                print("both")
            else :
                print("mack")
        else :
            if 17 in lst_set:
                print("zack")
            else:
                print("none")
        print()


if __name__ == "__main__" :
    main()