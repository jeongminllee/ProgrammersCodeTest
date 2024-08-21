N, D = map(int, input().split())
distances = [i for i in range(D+1)]
dp = []

for _ in range(N) :
    s, e, d = map(int, input().split())
    if e - s > d :
        dp.append((s, e, d))
dp.sort()

for s, e, d in dp :
    for i in range(1, D + 1) :
        if e == i :
            distances[i] = min(distances[i], distances[s] + d)
        else :
            distances[i] = min(distances[i], distances[i - 1] + 1)
print(distances[D])