T = int(input())
for test_case in range(1, T + 1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # [1] 종료시간 기준 오름차순 정렬
    arr.sort(key=lambda x:x[1])

    # [2] 한 작업씩 가능한지 체크, 처리
    ans = last = 0
    for s, e in arr :
        if last <= s :  # 배정 가능한 작업
            ans += 1
            last = e

    print(f"#{test_case} {ans}")