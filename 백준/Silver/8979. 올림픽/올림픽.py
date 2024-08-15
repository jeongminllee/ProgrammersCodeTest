N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

# 등수 계산
rank = 1
prev_medals = arr[0][1:]
for i, (country, gold, silver, bronze) in enumerate(arr) :
    if (gold, silver, bronze) != prev_medals :
        rank = i + 1
    if country == K :
        print(rank)
        break
    prev_medals = (gold, silver, bronze)