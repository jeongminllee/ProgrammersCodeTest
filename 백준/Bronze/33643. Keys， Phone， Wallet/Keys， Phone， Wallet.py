def main() :
    """
    keys, phone, wallet
    => 3개 다 있으면 ready
    """
    N = int(input())
    items = {
        "keys" : False,
        "phone" : False,
        "wallet" : False
    }
    res = []
    for _ in range(N) :
        item = input()
        if item in items.keys() and items[item] is False :
            items[item] = True

    for item, taken in items.items() :
        if taken is False :
            res.append(item)
            
    res.sort()

    if len(res) == 0 :
        print("ready")
    else :
        for ans in res :
            print(ans)


if __name__ == "__main__" :
    main()