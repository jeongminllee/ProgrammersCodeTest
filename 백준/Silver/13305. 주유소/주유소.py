N = int(input())
distance = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 현재까지의 최소 기름 가격을 첫 번째 도시의 가격으로 초기화합니다.
price = prices[0]

# 총 비용을 저장할 변수를 초기화합니다.
ans = 0

# 모든 도시를 순회합니다 (마지막 도시 제외).
for i in range(N - 1) :
    # 현재 도시의 기름 가격이 이전까지의 최소 가격보다 저렴하면 갱신합니다.
    if price > prices[i] :
        price = prices[i]

    # 현재까지의 최소 가격으로 다음 도시까지 가는데 필요한 기름을 구매합니다.
    ans += price * distance[i]

# 최종적으로 계산된 총 비용을 출력합니다.
print(ans)