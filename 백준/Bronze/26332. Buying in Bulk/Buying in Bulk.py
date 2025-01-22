n = int(input())
for _ in range(n) :
    # the number of items purchased by the customer, price for 1 item
    c, p = map(int, input().split())
    cnt = 0
    ans = 0

    # 1. No discount if you buy only one.
    # 2. $2 discount for each additional item if you buy more than one.
    while cnt != c :
        if cnt > 0:
            ans -= 2

        cnt += 1
        ans += p

    print(c, p)
    print(ans)