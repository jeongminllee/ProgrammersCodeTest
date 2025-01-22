def solve_party_transport(n, c, l, friends, cars) :
    # 지역별로 친구들 분류 (취한 사람, 안 취한 사람 구분)
    regions = {}

    for i, (region, state) in enumerate(friends) :
        if region not in regions :
            regions[region] = {'S' : [], 'I' : []}
        regions[region][state].append(i)

    # 지역별로 차량 분류
    cars_by_region = {}
    for i, (region, seats) in enumerate(cars) :
        if region not in cars_by_region :
            cars_by_region[region] = []
        cars_by_region[region].append(seats)

    total_cant_go = 0

    # 각 지역별로 처리
    for region in regions :
        sober = len(regions[region]['S'])   # 안 취한 사람의 수
        drunk = len(regions[region]['I'])   # 취한 사람의 수
        total_people = sober + drunk        # 해당 지역 전체 인원

        # 해당 지역으로 가는 차가 없는 경우 :
        if region not in cars_by_region :
            total_cant_go += total_people
            continue

        # 해당 지역 차량들의 총 좌석 수 계산
        available_cars = sorted(cars_by_region[region], reverse=True)   # 큰 차부터 처리
        total_seats = sum(available_cars)

        # 안 취한 사람들이 없는 경우 - 모두 귀가 불가
        if sober == 0 :
            total_cant_go += total_people
            continue
        people_can_go = 0
        remaining_drunk = drunk
        remaining_sober = sober

        # 각 차량별로 처리
        for seats in available_cars :
            if remaining_sober == 0 :   # 더 이상 운전할 사람이 없음
                break

            # 현재 차량에 태울 수 있는 사람 계산
            current_car_people = min(seats, remaining_drunk + remaining_sober)

            # 운전자 1명 할당
            remaining_sober -= 1
            current_car_people -= 1

            # 남은 자리에 최대한 취한 사람 배정
            drunk_in_car = min(remaining_drunk, current_car_people)
            remaining_drunk -= drunk_in_car
            current_car_people -= drunk_in_car

            # 그래도 자리가 남으면 안 취한 사람 배정
            sober_in_car = min(remaining_sober, current_car_people)
            remaining_sober -= sober_in_car

            # 이 차에 탑승하는 총 인원 누적
            people_can_go += drunk_in_car + sober_in_car + 1    # +1 은 운전자

        # 이 지역에서 못 가는 사람 수 계산
        total_cant_go += (total_people - people_can_go)

    return total_cant_go





def main():
    n, c, l = map(int, input().split())
    friends = []
    for _ in range(n) :
        region, state = input().split()
        friends.append((int(region), state))

    cars = []
    for _ in range(c) :
        region, seats = map(int, input().split())
        cars.append((region, seats))

    res = solve_party_transport(n, c, l, friends, cars)
    print(res)


T = int(input())
for t in range(1, T + 1):
    print(f'Data Set {t}:')
    main()