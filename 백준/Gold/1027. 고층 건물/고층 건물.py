def slope(x1, y1, x2, y2) :
    return (y2 - y1) / (x2 - x1)

N = int(input())
lst = list(map(int, input().split()))

res = [0] * N

for i in range(N-1) :
    max_slope = -float('inf')
    for j in range(i+1, N) :
        slope_ = slope(i, lst[i], j, lst[j])

        if slope_ <= max_slope :
            continue
        max_slope = max(max_slope, slope_)
        res[i] += 1
        res[j] += 1

print(max(res))