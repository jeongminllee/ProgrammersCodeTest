def main() :
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    cnt = 0         # 균형 잡힌 팀 개수
    best_sum = -1   # 최대 팀 레이팅
    l = 0

    for r in range(N) :
        # lst[r]를 최대값으로 가지는 구간을 만들기 위해 l 조정
        while l < r and lst[r] - lst[l] > M :
            l += 1

        # 현재 r을 최대값으로 쓸 수 있는 사람 수
        length = r - l  # [l ... r-1]에 있는 인원 수

        # 이 중에서 2명을 고르면, (r포함 3명 팀)
        if length >= 2 :
            # 새로 생기는 팀 개수: 조합 C(length, 2)
            cnt += length * (length - 1) // 2

            # 최대 팀 레이팅 갱신 (이 구간에서 가장 큰 세 명)
            candidate = lst[r] + lst[r-1] + lst[r-2]
            if candidate > best_sum :
                best_sum = candidate

    if cnt == 0 :
        print(-1)
    else :
        print(cnt, best_sum)

if __name__ == "__main__" :
    main()