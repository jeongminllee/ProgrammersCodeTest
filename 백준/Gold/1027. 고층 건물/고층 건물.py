N = int(input())
lst = list(map(int, input().split()))

res = [0] * N

for i in range(N-1) :
    max_slope = -float('inf')
    for j in range(i+1, N) :
        slope = (lst[j] - lst[i]) / (j - i)

        if slope <= max_slope :
            continue
        max_slope = max(max_slope, slope)
        res[i] += 1
        res[j] += 1

print(max(res))