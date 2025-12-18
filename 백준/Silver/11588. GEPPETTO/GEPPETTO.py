
N, M = map(int, input().split())
forbidden = set()

for _ in range(M) :
    a, b = map(int, input().split())
    forbidden.add((min(a-1, b-1), max(a-1, b-1)))

cnt = 0

for mask in range(1<<N) :
    valid = True

    selected = []
    for i in range(N) :
        if mask & (1 << i) :
            selected.append(i)

    for i in range(len(selected)) :
        for j in range(i + 1, len(selected)) :
            pair = (min(selected[i], selected[j]), max(selected[i], selected[j]))
            if pair in forbidden :
                valid = False
                break
        if not valid :
            break

    if valid :
        cnt += 1

print(cnt)