from collections import Counter
n = int(input())
arr = sorted(int(input()) for _ in range(n))

# 산술 평균
avg = round(sum(arr) / n)

# 중앙값
median = arr[n//2]

# 최빈값
mode = Counter(arr).most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1] :
    mode = mode[1][0]
else :
    mode = mode[0][0]

# 범위
range_ = arr[-1] - arr[0]

print(avg, median, mode, range_, sep='\n')