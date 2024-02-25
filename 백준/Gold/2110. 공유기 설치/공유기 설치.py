n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

start = 1
end = house[-1] - house[0]  # 최대 거리
answer = 0

while start <= end :
    mid = (start + end) // 2 # 중간 거리
    old = house[0]
    cnt = 1

    for i in range(1, len(house)) : # 공유기 위치 확인
        if house[i] >= old + mid :   # 이전 집에서 mid 만큼 떨어진 집에 공유기 설치
            cnt += 1
            old = house[i]

    if cnt >= c :   # 공유기를 충분히 설치할 수 있는 경우
        start = mid + 1
        answer = mid    # 최대 거리 저장

    else :  # 공유기를 충분히 설치할 수 없는 경우
        end = mid - 1

print(answer)