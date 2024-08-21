T = int(input())
for _ in range(T) :
    N = int(input())
    prices = list(map(int, input().split()))
    benefit = 0
    maxPrice = 0

    for i in range(N - 1, -1, -1) :
        if prices[i] > maxPrice :
            maxPrice = prices[i]
        else :
            benefit += maxPrice - prices[i]
    print(benefit)