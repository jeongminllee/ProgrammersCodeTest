def main() :
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    rating = 0
    res = 0

    for i in range(len(lst)-2) :
        for j in range(i+1, len(lst)-1) :
            for k in range(j+1, len(lst)) :
                team = [lst[i], lst[j], lst[k]]
                if max(team) - min(team) <= M :
                    res += 1
                    if rating < sum(team) :
                        rating = sum(team)
    if res == 0 :
        print(-1)
    else :
        print(f"{res} {rating}")


if __name__ == "__main__" :
    main()