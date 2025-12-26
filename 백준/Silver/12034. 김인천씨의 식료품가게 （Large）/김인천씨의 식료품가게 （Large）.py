T = int(input())

for t in range(1, T+1) :
    N = int(input())
    INU = list(map(int, input().split()))

    cnts = {}
    res = []

    for price in INU :
        if price not in cnts :
            cnts[price] = 1
        else :
            cnts[price] += 1

    for price in INU :
        if cnts[price] > 0 :
            res.append(price)
            cnts[price] -= 1

            original_price = (price//3) * 4
            cnts[original_price] -= 1

    print(f"Case #{t}:", *res)