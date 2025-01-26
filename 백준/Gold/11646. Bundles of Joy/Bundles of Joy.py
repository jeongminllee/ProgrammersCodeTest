def main() :
    n, m = map(int,input().split())

    high = [-1] * n
    cost = [0] * (m + 1)
    bundle = [[] for _ in range(m + 1)]
    bucket = [[] for _ in range(n + 1)] # bucket[k] : k개의 아이템을 가진 번들 리스트

    for i in range(m) :
        c, k, *items = map(int, input().split())
        items = [num-1 for num in items]
        cost[i] = c
        bundle[i] = items
        bucket[k].append(i)

    # 모든 아이템을 포함하는 가상의 번들 추가
    bundle[m] = list(range(n))
    cost[m] = 10 ** 9
    bucket[n].append(m)


    def process(i) :
        total = 0
        for item in bundle[i] :
            if high[item] == -1 :
                # 처음 방문한 아이템 : 현재 번들로 설정
                total = cost[i]
                high[item] = i
            else :
                prev = high[item]
                if prev != i :
                    # 다른 번들에 속한 경우 : 해당 번들 비용 추가 후 흡수
                    total += cost[prev]
                    # 이전 번들의 모든 아이템을 현재 번들로 이동
                    for j in bundle[prev] :
                        high[j] = i

        # 최소 비용 갱신
        if total != 0 :
            cost[i] = min(cost[i], total)

    # 각 버킷을 순회하며 번들 처리
    for k in range(n + 1) :
        for j in bucket[k] :
            process(j)

    print(cost[m])

T = int(input())
for _ in range(T) :
    main()