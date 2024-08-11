C = int(input())

for _ in range(C) :
    N, *score = map(int, input().split())
    cnt = 0

    mean = sum(score) // N
    for s in score :
        if s > mean :
            cnt += 1

    print(f"{cnt * 100 / N:.3f}%")