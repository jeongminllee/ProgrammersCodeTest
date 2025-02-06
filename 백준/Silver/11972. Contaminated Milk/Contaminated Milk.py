from collections import defaultdict

def find_min_medicine(N, M, D, S, party, sick) :
    drinks = defaultdict(set)   # 각 사람이 마신 우유 종류 저장
    sick_times = {} # 병에 걸린 사람과 그 시간 저장

    for p, m, t in party :
        drinks[p].add((m, t))

    for p, t in sick :
        sick_times[p] = t

    # 상한 우유 후보 찾기
    possible_bad_milk = set(range(1, M + 1))
    for p, sick_time in sick_times.items() :
        possible_milks = set()
        for m, t in drinks[p] :
            if t < sick_time :
                possible_milks.add(m)
        possible_bad_milk &= possible_milks # 모든 아픈 사람이 공통으로 마신 우유만 남김(교집합)

    # 최악의 경우 감염될 수 있는 최대 사람 수 찾기
    max_sick_count = 0
    for bad_milk in possible_bad_milk :
        infected = set()
        for p in range(1, N+1) :
            if any(milk == bad_milk for milk, time in drinks[p]) :
                infected.add(p)
        max_sick_count = max(max_sick_count, len(infected))

    return max_sick_count

def main() :
    N, M, D, S = map(int, input().split())

    party = [list(map(int, input().split())) for _ in range(D)]
    sick = [list(map(int, input().split())) for _ in range(S)]

    print(find_min_medicine(N, M, D, S, party, sick))

main()