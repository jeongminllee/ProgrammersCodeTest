def main() :
    """
    3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
    정원에 심는 꽃들의 수를 가능한 적게 한다.
    """
    N = int(input())    # 꽃의 총 개수
    flowers = []
    for _ in range(N) :
        y1, x1, y2, x2 = map(int, input().split())  # 피는 월, 일, 지는 월, 일
        start = y1*100 + x1
        end = y2*100 + x2
        flowers.append((start, end))

    flowers.sort()
    target_start = 301
    target_end = 1201

    curr = target_start
    idx = 0
    cnt = 0

    while curr < target_end :
        best_end = curr

        while idx < N and flowers[idx][0] <= curr :
            if flowers[idx][1] > best_end :
                best_end = flowers[idx][1]
            idx += 1

        if best_end == curr :
            print(0)
            return

        cnt += 1
        curr = best_end

    print(cnt)



if __name__ == "__main__" :
    main()