INF = 1 << 32

def compare(a, b) :
    return b if a < b else a

def main() :
    N = int(input())
    days = [(0, 0)] # 1-based indexing을 위한 더미 데이터

    max_happy = -1
    min_happy = INF
    max_fatigue = -1
    min_fatigue = INF

    # 각 날짜별 행복도와 피로도 입력
    for _ in range(N) :
        u, v = map(int, input().split())
        days.append((u, v))

    # youth 배열 계산 (앞에서부터)
    youth = [(0, 0)]
    for i in range(1, N + 1) :
        if days[i][0] != 0 and days[i][0] < min_happy :
            min_happy = days[i][0]
        if days[i][1] != 0 and days[i][1] > max_fatigue :
            max_fatigue = days[i][1]
        youth.append((min_happy, max_fatigue))

    # old 배열 계산 (뒤에서부터)
    old = [(0, 0)] * (N + 1)

    for i in range(N, 0, -1) :
        if days[i][0] != 0 and days[i][0] > max_happy :
            max_happy = days[i][0]
        if days[i][1] != 0 and days[i][1] < min_fatigue :
            min_fatigue = days[i][1]

        old[i] = (max_happy, min_fatigue)

    # 최적의 K 찾기
    cnt = -1
    for k in range(N - 1, -1, -1) : # k는 젊은 날
        youth_happy = youth[k][0]
        youth_fatigue = youth[k][1]
        old_happy = old[k+1][0]
        old_fatigue = old[k+1][1]


        if youth_happy > old_happy and youth_fatigue < old_fatigue :
            cnt = compare(cnt, k)

    print(cnt)

main()