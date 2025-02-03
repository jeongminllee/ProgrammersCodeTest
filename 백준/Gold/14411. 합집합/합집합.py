def main() :
    N = int(input())
    pos = [list(map(int, input().split())) for _ in range(N)]

    pos.sort(reverse=True)  # x를 기준으로 내림차순 정렬

    res = prev_y = 0

    for x, y in pos :
        if y > prev_y : # 현재 y 가 전 y 보다 클 경우
            res += x * (y - prev_y)
            prev_y = y
    print(res)
    
main()