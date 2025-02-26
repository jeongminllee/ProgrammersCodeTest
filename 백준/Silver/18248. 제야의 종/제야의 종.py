def sol_18248() :
    N, M = map(int, input().split())
    masks = []

    for _ in range(N) :
        row = list(map(int, input().split()))
        mask = 0
        for bit in row :
            mask = (mask << 1) | bit
        masks.append(mask)

    for i in range(N) :
        for j in range(i + 1, N) :
            if not ((masks[i] & masks[j] == masks[i]) or (masks[i] & masks[j] == masks[j])):
                print('NO')
                return
    print('YES')
sol_18248()